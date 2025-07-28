
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://spinnerlogger-uat.rockwool.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login_and_extract(driver):
    wait = WebDriverWait(driver, 20)

    email_login = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
    email_login.send_keys("azwana.ahmad@rockwool.com")

    sign_in_button = wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
    sign_in_button.click()

    # Wait for redirection and token to be available
    wait.until(lambda d: d.execute_script("return window.sessionStorage.getItem('access_token') !== null"))
    token = driver.execute_script("return window.sessionStorage.getItem('access_token');")

    user_name = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/div/app-top-nav/nav/div/div[2]/div[1]/div[1]"))).text
    user_opco = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/div/app-top-nav/nav/div/div[2]/div[1]/div[2]"))).text

    return {
        "token": token,
        "user_name": user_name,
        "user_opco": user_opco
    }

def test_token_result(login_and_extract):
    token = login_and_extract["token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get("https://graph.microsoft.com/v1.0/me", headers=headers)
    assert response.status_code == 200, f"Token validation failed. Status: {response.status_code}, Response: {response.text}"

def test_login_success(login_and_extract):
    assert login_and_extract["user_name"] == "AZWANA BINTI AHMAD (AZWBA)"f"Expected 'AZWANA BINTI AHMAD (AZWBA)', but got '{login_and_extract['user_name']}'"

def test_opco_display(login_and_extract):
    assert login_and_extract["user_opco"] == "DIGI" f"Expected 'DIGI', but got '{login_and_extract['user_opco']}'"

def test_image_display(driver):
    wait = WebDriverWait(driver, 10)
    user_image = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/div/app-top-nav/nav/div/div[2]/div[2]/img")))
    is_displayed = user_image.is_displayed()
    is_loaded = driver.execute_script(
        "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0", 
        user_image
    )
    assert is_displayed and is_loaded, "FAILED: PNG image is not displayed or not loaded properly"

