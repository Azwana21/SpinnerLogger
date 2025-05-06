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

#driver.find_element(By.ID,"i0116").send_keys("azwana.ahmad@rockwool.com")
#driver.find_element(By.ID,"idSIButton9").click()


#To verify successfully login to OVERVIEW screen
#XPATH - //tagname[@attribute='value'] -> //input[@type='submit'] 

user_name = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//")))




time.sleep (20)