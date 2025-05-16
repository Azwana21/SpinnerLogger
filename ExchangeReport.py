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

email_login = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"i0116")))
email_login.send_keys("azwana.ahmad@rockwool.com")

sign_in_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"idSIButton9")))
sign_in_button.click()




time.sleep(20)

#click the Factory drop-down to expand
factory_select = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div/div/app-homepage/div/div/form/div/div[1]/div[1]/mat-form-field"))).click()

#select MOS in Factory drop-down list

factory_select_MOS = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div[2]/div/div/div/mat-option[3]/span"))).click()

time.sleep(20)


