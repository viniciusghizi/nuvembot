import traceback, logging, sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from variables import constants as consts
from scripts.utils.firefox_option import firefox_option
from scripts.utils import notifications as WhatsappService
from scripts.orders import nuvemshop as NuvemshopService
from messages import messages as Messages

def open_browser(message : Messages):

    logging.warning(message['WARN_OPEN_BROWSER'])

    OPTIONS = firefox_option()
    driver = webdriver.Firefox(options=OPTIONS)
    
    return  driver

def try_login_shop(message : Messages):
    for attempt in consts.MAX_RETRIES_LOGIN:
        DRIVER = open_browser(message)
        try:
            PEDIDOS = NuvemshopService.check_created_orders(DRIVER, message)
            
            return PEDIDOS
        except Exception:
            logging.error(f"{message['ERROR_ATTEMPT_LOGIN']} {attempt + 1}")
            logging.error(traceback.format_exc())
            
    logging.warning(message['ERROR_ATTEMPT_LOGIN'])

def get_orders(message: Messages):
    logging.warning(message['INFO_INITIALIZE'])
    logging.warning(message['WARN_MAIN_GETTING_ORDERS'])
    PEDIDOS = try_login_shop(message)
    
    if len(PEDIDOS) == 0:
        logging.warning(message['WARN_MAIN_NOT_FOUND_NEW_ORDERS'])
        return
    logging.warning(message['INFO_END'])


if __name__ == '__main__':
    language = consts.LANGUAGE_PT if 'pedidos' in sys.argv else consts.LANGUAGE_US
    get_orders(Messages.messages[language])


