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

time.sleep (30)
print(driver.execute_script("return Object.keys(window.localStorage);"))


token_key = "5a71239f-0f50-4d3e-a92e-61ab9876e670.ec85c1f0-148f-4d0f-b9f5-bfd62a99ed8c-login.windows.net-accesstoken-4d78dd4e-0c46-4b19-af19-8064e4dc060f-ec85c1f0-148f-4d0f-b9f5-bfd62a99ed8c-http://fof-spinnerloggerapp-t-euw-001-svc_azureadauth-sp.rwgroup.org/default.write--"


token_json = driver.execute_script(f"return window.localStorage.getItem('{token_key}');")
print("Raw token JSON:", token_json)


import json

token_data = json.loads(token_json)
access_token = token_data.get("secret")
print("Access token:", access_token)


import requests

headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get("https://your-api.com/protected-endpoint", headers=headers)

if response.status_code == 200:
    print("✅ Token is valid.")
else:
    print("❌ Token is invalid or expired.")


time.sleep (10)