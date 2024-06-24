from pyshadow.main import Shadow
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

import logging, time
import urllib.parse 
import  classes.order_class as Order

from variables.constants import PHONE,X_SEND_MESSAGE_BUTTON


def whatsapp_notification(driver: WebDriver,message):
    driver.get("https://web.whatsapp.com")
    time.sleep(5)
    
    receiver = PHONE + urllib.parse.quote_plus(str(message)) 
    driver.get(receiver)
    while len (driver.find_elements(By.ID, 'side')) < 1:
        time.sleep(1)
        logging.warn("Waiting Whatsapp")
    
    time.sleep(15)
    
    button = driver.find_element(By.XPATH, X_SEND_MESSAGE_BUTTON )

    button.click()
    
    

    logging.warn(f"Sended message to Whatsapp: {message} ")
    


    