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

#Access Factory drop-down list

factory_value = WebDriverWait (driver, 10). until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div/div/app-reports-list/div/div/div/form/div[1]/div/mat-form-field/div/div[1]/div/mat-select"))).click()

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

#To click the checkbox 
VAM_checked = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div[2]/div/div/div/mat-option[2]/mat-pseudo-checkbox"))).click()

#To locate the checkbox element again to check it's state
VAM_checkbox = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/div/mat-option[2]/mat-pseudo-checkbox")
VAM_checkbox_class = VAM_checkbox.get_attribute("class")

#Validate of the checbox has been selected
if "mat-pseudo-checkbox-checked" in VAM_checkbox_class:
    print("VAM Checkbox is selected")
else:
    print("VAM Checkbox is not selected")

#Validate the VAM is available in the drop-down
assert factory_value_text == "VAM", f"Expected 'VAM', but value '{factory_value_text}'"
print("Validation successful: VAM is available in the drop-down Factory")


#Get text of the Factory Drop-down: ROE
factory_value_ROE = WebDriverWait (driver, 10). until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div/div/mat-option[3]/span")))
factory_value_text = factory_value_ROE.text

print({factory_value_text})

#To click the checkbox 
ROE_checked = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div[2]/div/div/div/mat-option[3]/mat-pseudo-checkbox"))).click()

#To locate the checkbox element again to check it's state
ROE_checkbox = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/div/mat-option[3]/mat-pseudo-checkbox")
ROE_checkbox_class = ROE_checkbox.get_attribute("class")

#Validate of the checbox has been selected
if "mat-pseudo-checkbox-checked" in ROE_checkbox_class:
    print("ROE Checkbox is selected")
else:
    print("ROE Checkbox is not selected")


#Validate the ROE is available in the drop-down
assert factory_value_text == "ROE", f"Expected 'ROE', but value '{factory_value_text}'"
print("Validation successful: ROE is available in the drop-down Factory")

# Get text of the Factory drop_down : MOS
factory_value_MOS = WebDriverWait (driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div[2]/div/div/div/mat-option[4]/span")))
factory_value_text = factory_value_MOS.text

print({factory_value_text})

#To click the checkbox
MOS_checked = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div[2]/div/div/div/mat-option[4]/mat-pseudo-checkbox"))).click()

#To locate the checkbox element again to check it's state
MOS_checkbox = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/div/mat-option[4]/mat-pseudo-checkbox")
MOS_checkbox_class = MOS_checkbox.get_attribute("class")

#Validate the checkbox has been selected
if "mat-pseudo-checkbox-checked" in MOS_checkbox_class:
    print("MOS Checkbox is selected")
else:
    print("MOS Checkbox is not selected")

#Validate the MOS is available in the drop-down
assert factory_value_text == "MOS", f"Expected 'MOS', but value '{factory_value_text}'"
print("Validation Successful: MOS is available in the drop-down Factory")

#Get text of the Factory drop-down : SEL
factory_value_SEL = WebDriverWait (driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div[2]/div/div/div/mat-option[5]/span")))
factory_value_text = factory_value_SEL.text

print({factory_value_text})

#To click the checkbox
SEL_checked = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div[2]/div/div/div/mat-option[5]/mat-pseudo-checkbox"))).click()

#To locate the checkbox element again to check it's state
SEL_checkbox = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/div/mat-option[5]/mat-pseudo-checkbox")
SEL_checkbox_class = SEL_checkbox.get_attribute("class")

#Validate the checkbox has been selected
if "mat-pseudo-checkbox-checked" in SEL_checkbox_class:
    print("SEL checkbox is selected")
else:
    print("SEL Checkbox is not selected")

#Validate the SEL is available in the drop-down
assert factory_value_text =="SEL", f"Expected 'SEL', but value '{factory_value_text}"
print("Validate Successful: SEL is avilable in the drop-down Factory")
time.sleep (20)