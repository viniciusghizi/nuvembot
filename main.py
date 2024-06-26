import traceback, logging, sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from variables import constants as consts
from scripts.utils.firefox_option import firefox_option
from scripts.utils import notifications as NotificationService
from scripts.orders import nuvemshop as NuvemshopService
from dictionary import messages as Dictionary

def open_browser(message : Dictionary):

    logging.warning(message['WARN_OPEN_BROWSER'])

    OPTIONS = firefox_option()
    driver = webdriver.Firefox(options=OPTIONS)
    
    return  driver

def try_login_shop(message : Dictionary):
    for attempt in consts.MAX_RETRIES_LOGIN:
        DRIVER = open_browser(message)
        try:
            PEDIDOS = NuvemshopService.check_created_orders(DRIVER, message)
            
            return PEDIDOS
        except Exception:
            logging.error(f"{message['ERROR_ATTEMPT_LOGIN']} {attempt + 1}")
            logging.error(traceback.format_exc())
            
    logging.warning(message['ERROR_ATTEMPT_LOGIN'])

def get_orders(message: Dictionary):
    logging.warning(message['INFO_INITIALIZE'])
    driver = open_browser(message)
    logging.warning(message['WARN_MAIN_GETTING_ORDERS'])
    ORDERS = NuvemshopService.check_created_orders(driver, message)
    
    if len(ORDERS) == 0:
        logging.warning(message['WARN_MAIN_NOT_FOUND_NEW_ORDERS'])
        NotificationService.whatsapp_notification( driver, message['MESSAGE_ORDER_NOT_FOUNDED'], message )
    else:
        NuvemshopService.print_order( driver, message )
        NotificationService.whatsapp_notification( driver , message['INFO_NOTIFICATION_ORDER_CHECKED'], message )
        NotificationService.whatsapp_notification( driver , ORDERS, message )
    return True
    
if __name__ == '__main__':
    language = consts.LANGUAGE_PT if 'pedidos' in sys.argv else consts.LANGUAGE_US
    get_orders(Dictionary.messages[language])


