
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from variables.constants import ID_USER_NUVEM,X_HOME_NUVEM, X_HOME_SUPPLIER

def login(username_element, password_element, username, password, DRIVER):
    wait =WebDriverWait(DRIVER, 580)
    wait.until(EC.element_to_be_clickable((By.ID, username_element)))

    username_input = DRIVER.find_element(By.ID, username_element)
    password_input = DRIVER.find_element(By.ID, password_element)
    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

    if username_element == ID_USER_NUVEM:
        wait.until(EC.element_to_be_clickable((By.XPATH, X_HOME_NUVEM)))
    else:
        wait.until(EC.element_to_be_clickable((By.XPATH, X_HOME_SUPPLIER)))
    
    return True
