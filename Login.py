import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Chrome driver service

driver = webdriver.Chrome()
driver.get("https://spinnerlogger-uat.rockwool.com/")

driver.maximize_window()
print(driver.title)
print(driver.current_url)

#Login to Spinner Logger (Authorization SSO)
time.sleep (5)

email_login = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"i0116")))
email_login.send_keys("azwana.ahmad@rockwool.com")

sign_in_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"idSIButton9")))
sign_in_button.click()

time.sleep (20)


#Wait for redirection and extract token
time.sleep(5)
token = driver.execute_script("return window.sessionStorage.getItem('access_token');")
print("Extract Token:",token)




#Validate token by calling a protected API
headers = {
    "Authorization": f"Bearer {token}"
}
response = requests.get("https://login.microsoftonline.com/ec85c1f0-148f-4d0f-b9f5-bfd62a99ed8c/oauth2/v2.0/token", headers=headers)

if response.status_code == 200:
    print("✅ Token is valid. Access granted")
else:
    print(f"❌ Token validation failed. Status:{response.status_code}")
    print(response.json())


#To validate if the name is correct

user_name = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div/app-top-nav/nav/div/div[2]/div[1]/div[1]")))

#Get text of the element
user_name_text = user_name.text

#Validate the username logged in the system
assert user_name_text == "AZWANA BINTI AHMAD (AZWBA)", f"Expected 'AZWANA BINTI AHMAD (AZWBA)', but value '{user_name_text}'"

print("✅ Validation successful: The user name is correct")

#Validate if the OPCO display is correct
user_opco = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div/app-top-nav/nav/div/div[2]/div[1]/div[2]")))

#Get text of the OPCO element
user_opco_text = user_opco.text

#Validate if the OPCO is correct
assert user_opco_text == "DIGI", f"Expected 'DIGI', but value '{user_opco_text}'"

print("✅ Validation successful: The user OPCO is correct")


#Validate if the user image is display.
user_image = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div/app-top-nav/nav/div/div[2]/div[2]/img")))

#Validate the image is display in the UI.

is_displayed = user_image.is_displayed()

#validate if the image is completly loaded using javascript


is_loaded = driver.execute_script("return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0", user_image)


#Final image validation
if is_displayed and is_loaded:
    print ("✅ Validation successful: PNG image is displayed and loaded successfully")

else:
    print("❌ Validation Failed: PNG image is not displayed or not loaded properly")

time.sleep (20)

