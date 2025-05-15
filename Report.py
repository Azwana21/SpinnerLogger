import time
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

time.sleep(3)
email_login = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"i0116")))
email_login.send_keys("azwana.ahmad@rockwool.com")

sign_in_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"idSIButton9")))
sign_in_button.click()

#Go to REPORTS screen
report_page  = WebDriverWait (driver,10).until(EC.visibility_of_element_located((By.XPATH,"//app-top-nav/nav/div/nav/div/div/div/a[3]"))).click()

#Check if the value is available in the Factory drop-down list.

factory_value = WebDriverWait (driver, 10). until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div/div/app-reports-list/div/div/div/form/div[1]/div/mat-form-field/div/div[1]/div/mat-select/div/div[1]"))).click()

#To print out all value in Factory drop-down

#Get text of the Factory Drop-down: All factories
factory_value_AllFactory = WebDriverWait (driver, 10). until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div/div/mat-option[1]/span")))
factory_value_text = factory_value_AllFactory.text

print({factory_value_text})

#Validate the All Factory is available in the drop-down
assert factory_value_text == "All factories", f"Expected 'All factories', but value '{factory_value_text}'"

print("Validation successful: All factories is available in the drop-down FACTORY")

#Get text of the Factory Drop-down: VAM
factory_value_VAM = WebDriverWait (driver, 10). until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div/div/mat-option[2]/span")))
factory_value_text = factory_value_VAM.text

print({factory_value_text})

#Validate the VAM is available in the drop-down
assert factory_value_text == "VAM", f"Expected 'All factories', but value '{factory_value_text}'"
print("Validation successful: VAM is available in the drop-down Factory")


#Get text of the Factory Drop-down: ROE
factory_value_ROE = WebDriverWait (driver, 10). until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div/div/mat-option[2]/span")))
factory_value_text = factory_value_VAM.text

print({factory_value_text})

#Validate the ROE is available in the drop-down
assert factory_value_text == "ROE", f"Expected 'All factories', but value '{factory_value_text}'"

print("Validation successful: ROE is available in the drop-down Factory")

time.sleep (20)