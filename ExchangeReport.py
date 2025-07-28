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

time.sleep(10)
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


#Click the Line drop-down to expand
line_select = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div/div/app-homepage/div/div/form/div/div[1]/div[2]/mat-form-field/div/div[1]/div/mat-select/div/div[1]/span"))).click()


#Select 47001001 in Line drop-down list

line_select_MOS = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div[2]/div/div/div/mat-option/span"))).click()

time.sleep(10)

#Click the Spinner drop-down to expand

spinner_select = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div/div/app-homepage/div/div/form/div/div[1]/div[3]/mat-form-field/div/div[1]/div/mat-select/div/div[1]"))).click()

#Select Z30 in the Spinner ID drop-down list

spinner_select_Z10 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div[2]/div/div/div/mat-option[4]/span"))).click()

time.sleep(10)

#Validate if the Total runtime for spinner is display

total_runtime = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div/div/app-homepage/div/div/form/div/div[2]/div[1]/mat-card/div/div[1]/span")))


#Get value of the total runtime element
total_runtime_value = total_runtime.text

if total_runtime_value.strip():
    print("PASSED:Total runtime is displayed")
    print("Total Runtime Value:", total_runtime_value)
else:
    print("FAILED: Total runtime is not visible in the UI")

time.sleep(10)

#Validate if the runtime of component

runtime_rotor = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div/div/app-homepage/div/div/form/div/div[2]/div[1]/mat-card/div/div[2]/div[1]/div[2]/mat-table/mat-row[3]/mat-cell[2]/div")))

#Get value of the runtime

runtime_rotor_value = runtime_rotor.text

if runtime_rotor_value.strip():
    print("PASSED: Runtime hours is displayed")
    print("Runtime hours value is:",runtime_rotor_value)
else:
    print("FAILED: Runtime hours is not visible in the UI")

#Go to Exchange report

exchange_report = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div/div/app-homepage/div/div/form/div/div[2]/div[1]/mat-card/div/div[2]/div[1]/div[2]/mat-table/mat-row[3]/mat-cell[3]/div"))).click()

#To verify if application go to new exchange report .

exchange_report_title = driver.find_element(By.XPATH,"/html/body/app-root/div/div/app-exchange-component/app-top-title-bar/div/div/div/div[1]/div[2]")

text = exchange_report_title.text

print("Page Title:",text)

if "COMPONENT EXCHANGE" in text:
    print("PASSED: The Exchange Report page is fully loaded")
else:
    print("FAILED: Failed to load the Exchange report page")

time.sleep(20)

#Fill in the Exchange report

import random

work_id = random.randint(1,9999)

driver.find_element(By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[1]/div[1]/div[2]/mat-form-field/div/div[1]/div/input").send_keys("Auto Test", work_id)

damage_type = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[1]/div[2]/div[2]/mat-form-field"))).click()

damage_type_corrosion = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[2]/div/div/div/mat-option[12]/span"))).click()

damage_cause = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[1]/div[3]/div[2]/mat-form-field"))).click()

damage_cause_other = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[2]/div/div/div/mat-option[6]/span"))).click()

damage_location = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[1]/div[4]/div[2]/mat-form-field"))).click()

damage_location_other = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[2]/div/div/div/mat-option[5]/span"))).click()

removal_date = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[1]/div[5]/div[2]/mat-form-field/div/div[1]/div[2]/mat-datepicker-toggle/button"))).click()

select_removal_date = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[2]/div/mat-dialog-container/ngx-mat-datetime-content/div[2]/button"))).click()

part_id = random.randint(10,90)

driver.find_element(By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[1]/div[6]/div[2]/mat-form-field/div/div[1]/div/input").send_keys("Auto Part ID Test",part_id)

detail_desc = driver.find_element(By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[2]/div[1]/div[2]/mat-form-field/div/div[1]/div/textarea").send_keys ("This is a test automation for description of exchange report")

upload_document = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[2]/div[2]/div[2]/app-file-upload/div/div/div[1]/rw-button/button"))).click()

time.sleep (5)

file_upload = driver.find_element(By.ID,"file")
file_upload.send_keys("C:\\Users\\azwba\\OneDrive - ROCKWOOL Group\\Documents\\Spinner Logger\\Test Data\\png-5mb-1.png")
file_upload_upload = file_upload.click


#time.sleep (10)
#Verify if the upload is successfull
#file_upload_done = driver.find_element(By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[2]/div[2]/div[2]/app-file-upload/div/div/div[2]").text

file_upload_done = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[2]/div[2]/div[2]/app-file-upload/div/div/div[2]"))).text



if "png-5mb-1.png" in file_upload_done:
    print ("PASSED: File is successfully uploaded")
    print("File Name :",file_upload_done )
else:
    print("FAILED: Upload failed as file is not visible in UI")


#Delete upload file

file_delete = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[2]/div[2]/div[2]/app-file-upload/div/div/div[2]/div/div/div[2]/rw-button/button/span"))).click()


#file_delete = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,""))).click()

#/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[2]/div[2]/div[2]/app-file-upload/div/div/div[2]


confirmation_delete = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[2]/div/mat-dialog-container/confirmation-dialog/div/div/rw-button[2]/button"))).click()


#wait for popup container to appear
delete_popup = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CLASS_NAME,"notification-snack")))

#Get the message text
success_delete_message = delete_popup.find_element(By.CLASS_NAME,"msg-container").get_attribute("innerText")

#verify the full message
expected_text = "File removed"
actual_text = f"{success_delete_message}"
assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"

print("Popup message verified successfully")






time.sleep(20)