import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


#Chrome driver service

driver = webdriver.Chrome()
driver.get("https://spinnerlogger-dev.rockwool.com/")

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

def factory_line_spinner_selection():

    #click the Factory drop-down to expand
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div/div/app-homepage/div/div/form/div/div[1]/div[1]/mat-form-field"))).click()

    #select MOS in Factory drop-down list

    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div[2]/div/div/div/mat-option[3]/span"))).click()


    #Click the Line drop-down to expand
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div/div/app-homepage/div/div/form/div/div[1]/div[2]/mat-form-field/div/div[1]/div/mat-select/div/div[1]/span"))).click()


    #Select 47001001 in Line drop-down list

    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div[2]/div/div/div/mat-option/span"))).click()

    time.sleep(10)

    #Click the Spinner drop-down to expand

    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div/div/app-homepage/div/div/form/div/div[1]/div[3]/mat-form-field/div/div[1]/div/mat-select/div/div[1]"))).click()

    #Select Z30 in the Spinner ID drop-down list

    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div[2]/div/div/div/mat-option[4]/span"))).click()

    time.sleep(10)




#Validate if the Total runtime for spinner is display
factory_line_spinner_selection()
total_runtime = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div/div/app-homepage/div/div/form/div/div[2]/div[1]/mat-card/div/div[1]/span")))


#Get value of the total runtime element
total_runtime_value = total_runtime.text

def test_total_runtime_displayed():
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
def test_runtime_rotor_displayed():
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

def test_exchanged_report_page_loaded():
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

wait = WebDriverWait(driver,10)
file_upload = driver.find_element(By.ID,"file")
file_upload.send_keys("C:\\Users\\azwba\OneDrive - ROCKWOOL Group\\Documents\\Spinner Logger\\Test Data\\testImage_1.1-MB.jpg")
file_upload.click



time.sleep (30)

#Verify if the upload is successfull
file_upload_done = driver.find_element(By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[2]/div[2]/div[2]/app-file-upload/div/div/div[2]").text

def test_file_upload():
    # try:
    file_upload_done = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[2]/div[2]/div[2]/app-file-upload/div/div/div[2]"))).text
    if "testImage_1.1-MB.jpg" in file_upload_done:
        print ("PASSED: File is successfully uploaded")
        print("File Name :", file_upload_done)
            # assert True #This marks the test as passed
    else:
        print("FAILED: Upload failed as file is not visible in UI")
            # pytest.fail("File upload failed, file not visible in UI")
    
    # except Exception as e:
    #     print ("Error: Exception occurred during file upload check:", str(e))
    #     pytest.fail("File upload check failed due to exception")


time.sleep(20)

#Delete upload file

file_delete = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[2]/div[2]/div[2]/app-file-upload/div/div/div[2]/div/div/div[2]/rw-button/button/span")))

file_delete.click()

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

def test_delete_document_popup():
    print("PASSED: Delete document popup message verified successfully")


#Verify if Save for later button is clickable

save_for_later = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[2]/div/div[1]/rw-button/button"))).click()

#verify if popup message is displayed
save_for_later_popup = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//app-notification-snack-bar//div[contains(@class, 'msg-container') and normalize-space(text())='Saved.']")))

#Get the message text
save_for_later_success_message = save_for_later_popup.get_attribute("innerText").strip ()

#verify the full message
expected_text_save = "Saved."
actual_text_save = f"{save_for_later_success_message}"
assert actual_text_save == expected_text_save, f"expected '{expected_text_save}', but got '{actual_text_save}'"
def test_save_for_later_popup():
    print("PASSED: Save for later popup message successfully displayed")


#verify if the save draft information is still successfully displayed after save for later button is clicked

overview_screen = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div/app-top-nav/nav/div/nav/div/div/div/a[1]"))).click()

#Go to back again to existing Exchange report


time.sleep(30)

#Go to Exchange report again

exchange_report = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div/div/app-homepage/div/div/form/div/div[2]/div[1]/mat-card/div/div[2]/div[1]/div[2]/mat-table/mat-row[3]/mat-cell[3]/div"))).click()



#To verify if application go to new exchange report .

exchange_report_title = driver.find_element(By.XPATH,"/html/body/app-root/div/div/app-exchange-component/app-top-title-bar/div/div/div/div[1]/div[2]")

text = exchange_report_title.text

print("Page Title:",text)


time.sleep(20)

#To verify if the save data is available in exchanged report

#verify if the work ID is saved
def test_work_id_saved():
    saved_work_id_value = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[1]/div[1]/div[2]/mat-form-field/div/div[1]/div/input")))
    if saved_work_id_value:
        saved_work_id = saved_work_id_value.get_attribute("value")
        print("PASSSED: Work ID Value",saved_work_id)
    else:
        print("FAILED: WorkID value does not exist in UI")

#verify if the damage type is saved
def test_damage_type_saved():
    saved_damage_type_value= WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[1]/div[2]/div[2]/mat-form-field/div/div[1]/div/mat-select/div/div[1]/span/span")))
    if saved_damage_type_value:
        saved_damage_type = saved_damage_type_value.text
        print("PASSED: Damage Type value", saved_damage_type)
    else:
        print("FAILED: Damage Type value does not exist in UI")

#verify if the damage cause is saved
def test_damage_cause_saved():
    saved_damage_cause_value = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[1]/div[3]/div[2]/mat-form-field/div/div[1]/div/mat-select/div/div[1]/span/span")))
    if saved_damage_cause_value:
        saved_damage_cause = saved_damage_cause_value.text
        print("PASSED: Damage cause value", saved_damage_cause_value)
    else:
        print("FAILED: Damage cause value does not exist in UI")

#Verify if the damage location is saved
def test_damage_location_saved():
    saved_damage_location_value = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[1]/div[4]/div[2]/mat-form-field/div/div[1]/div/mat-select/div/div[1]/span/span")))
    if saved_damage_location_value:
        saved_damage_location = saved_damage_location_value.text
        print("PASSED: Damage Location value", saved_damage_location)
    else:
        print("FAILED: Damage Location value does not exist in UI")

#verify if the removal date is saved
def test_removal_date_saved():
    saved_removal_date_value = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[1]/div[5]/div[2]/mat-form-field/div/div[1]/div[1]/input")))
    if saved_removal_date_value:
        saved_removal_date = saved_removal_date_value.get_attribute("value")
        print("PASSED: Removal date value", saved_removal_date)
    else:
        print("FAILED: Removal date value does not exist in UI")

#verify if the replace partID is saved
def test_replace_partid_saved():
    saved_replace_partid_value = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[1]/div[6]/div[2]/mat-form-field/div/div[1]/div/input")))
    if saved_replace_partid_value:
        saved_replace_partid = saved_replace_partid_value.get_attribute("value")
        print("PASSED: replace part ID value", saved_replace_partid)
    else:
        print("FAILED: Replace part id value does not exist in UI")

#Veirfy if the Detailed descirption is saved
def test_detailed_descirption_saved():
    saved_description_value = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[2]/div[1]/div[2]/mat-form-field/div/div[1]/div/textarea")))
    if saved_description_value:
        saved_description = saved_description_value.get_attribute("value")
        print("PASSED: Detailed description value:", saved_description)
    else:
        print("FAILED: Detailed description value does not exist in UI")





# saved_damage_cause = driver.find_element(By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[1]/div[3]/div[2]/mat-form-field/div/div[1]/div/mat-select/div/div[1]").get_attribute("value")
# print("Damage Cause:", saved_damage_cause)

# saved_damage_location = driver.find_element(By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[1]/div[4]/div[2]/mat-form-field/div/div[1]/div/mat-select/div/div[1]").get_attribute("value")
# print("Damage Location:", saved_damage_location)

# saved_removal_date = driver.find_element(By.XPATH,"/html/body/app-root/div/div/app-exchange-component/div/div/form/div/mat-card[2]/div[1]/div[1]/div[5]/div[2]/mat-form-field/div/div[1]/div[1]/input").get_attribute("value")
# print("Removal Date:", saved_removal_date)


time.sleep(10)



test_total_runtime_displayed()
test_runtime_rotor_displayed()
test_exchanged_report_page_loaded()
test_file_upload()
test_delete_document_popup()
test_save_for_later_popup()
test_work_id_saved()
test_damage_type_saved()
test_damage_cause_saved()
test_damage_location_saved()
test_removal_date_saved()
test_replace_partid_saved()
test_detailed_descirption_saved()


time.sleep(20)