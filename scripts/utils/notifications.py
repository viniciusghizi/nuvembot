from pyshadow.main import Shadow
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

import logging, time
import urllib.parse 
import  classes.order_class as Order

from variables.constants import PHONE,X_SEND_MESSAGE_BUTTON, LANGUAGE_US, LANGUAGE_PT
from messages import messages as Messages


def whatsapp_notification(driver: WebDriver, send_message, message: Messages):
    
    
    driver.get("https://web.whatsapp.com")
    time.sleep(10)
    
    receiver = f"https://web.whatsapp.com/send/?phone={PHONE}&text={urllib.parse.quote_plus(str(send_message))}" 
    driver.get(receiver)
    while len (driver.find_elements(By.ID, 'side')) < 1:
        time.sleep(1)
        logging.warn(message['WARN_NOTIFICATION_WAITING_WHATSAPP'])
    
    time.sleep(10)
    
    button = driver.find_element(By.XPATH, X_SEND_MESSAGE_BUTTON )
    button.click()

    i = 0
    while i < 91:
        time.sleep(1)
        logging.warn(f"{message['WARN_NOTIFICATION_SENDING_WAITING_TIME']} {i} ")
        i = i + 1

    logging.warn(f"{message['WARN_NOTIFICATION_SENDING_CONFIRM_MESSAGE']} {send_message} ")