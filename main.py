import traceback, logging, sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from variables import constants as consts
from scripts.orders.nuvemshop import consult_created_orders
from scripts.utils.notifications import whatsapp_notification

MAX_TENTATIVAS_VER_EMAIL = range(2)

def acessar_browser():

    logging.info("Acessando Navegador")

    OPTIONS = webdriver.FirefoxOptions()
    

    if not consts.GRAPHIC_INTERFACE:
        OPTIONS.add_argument("-headless")
    
    OPTIONS.set_preference("layers.acceleration.disabled", True)
    OPTIONS.set_preference("layers.acceleration.force-enabled", False)
    OPTIONS.set_preference("dom.ipc.processCount", 1)
    OPTIONS.set_preference("browser.cache.memory.capacity", 4096)
    OPTIONS.set_preference("browser.sessionhistory.max_entries", 1)
    OPTIONS.set_preference("permissions.default.image", 2)
    OPTIONS.binary_location = '/snap/firefox/4451/usr/lib/firefox/firefox'
    OPTIONS.profile = '/home/viniciusghizi/snap/firefox/common/.mozilla/firefox/ovnyk8my.default'

    driver = webdriver.Firefox(options=OPTIONS)
    return  driver

def tentativas_login_loja():
    for tentativa in MAX_TENTATIVAS_VER_EMAIL:
        DRIVER = acessar_browser()

        try:
            PEDIDOS = consult_created_orders(DRIVER)
            
            return PEDIDOS

        except Exception:
            numero_execucao = tentativa + 1
            logging.error(f"FALHA {numero_execucao} ao tentar obter PEDIDOS")
            logging.error(traceback.format_exc())
            

    logging.warning("FALHA EM TODAS TENTATIVAS DE OBTER PEDIDOS")

def get_orders():
    logging.warning("Consulting Orders.")
    PEDIDOS = tentativas_login_loja()
    
    if len(PEDIDOS) == 0:
        logging.warning("We don't have new orders")
        return

    logging.warning("3 - Creating orders on supplier")
    


if __name__ == '__main__':
    logging.warning("INITIALIZING.")
    if 'pedidos' in sys.argv:
        get_orders()

