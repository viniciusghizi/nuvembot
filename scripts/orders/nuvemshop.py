from pyshadow.main import Shadow
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from classes.order_class import order_class as Order
import logging, time

from variables.constants import URL_NUVEMSHOP,ID_USER_NUVEM, ID_PASS_NUVEM, USER_NUVEMSHOP,PASS_NUVEMSHOP,URL_CONFIRMED_PAYMENT, X_ORDER_NUMBER, X_ORDER_DETAIL_NAME, X_ORDER_DETAIL_VARIATION, X_ORDER_DETAIL_QUANTITY, X_EMBALADO_BUTTON, X_PRODUCTS_QUANTITY, MESSAGE_ORDER_CHECKED, MESSAGE_ORDER_NOT_FOUNDED
from scripts.login import login
from scripts.utils.notifications import whatsapp_notification


def consult_created_orders(driver: WebDriver) :
    
    driver.get(URL_NUVEMSHOP)
    logging.warning("1 - Logging NUVEMSHOP")
    
    login( ID_USER_NUVEM , ID_PASS_NUVEM , USER_NUVEMSHOP , PASS_NUVEMSHOP ,  driver )

    orders = get_order( driver )

    if len(orders) > 0:
        print_order(driver)
        whatsapp_notification( driver , MESSAGE_ORDER_CHECKED )
        whatsapp_notification( driver , orders )
    
    else :
        whatsapp_notification( driver, MESSAGE_ORDER_NOT_FOUNDED )

def print_order(driver: WebDriver) :
    url = driver.current_url 
    driver.get(url.replace("v2/orders/","orders/packing_slip/"))

    logging.warning("3 - Printing Order")
    driver.execute_script("window.print()")
    
    logging.warning("4 - Print finished")

def update_order(driver: WebDriver) :
    return driver.find_element(By.XPATH, X_EMBALADO_BUTTON).click()

def get_order(driver: WebDriver):
    driver.get(URL_CONFIRMED_PAYMENT)
    logging.warning("2 - Getting Order Details")
    
    time.sleep(5)

    order_number = driver.find_element( By.XPATH, X_ORDER_NUMBER ) 
    order_number.click()
    
    time.sleep(5)

    max_quantity = driver.find_element(By.XPATH, X_PRODUCTS_QUANTITY).text.split(" ")[0]
    orders = []
    
    for i in range(int(max_quantity)):
        item_name = driver.find_element( By.XPATH,X_ORDER_DETAIL_NAME.replace( "#" , str(i+1) ) ).text
        item_quantity = driver.find_element( By.XPATH,X_ORDER_DETAIL_QUANTITY.replace("#", str(i+1) ) ).text.split("x")[0]
        item_variation = driver.find_element( By.XPATH,X_ORDER_DETAIL_VARIATION.replace("#", str(i+1) ) ).text.split(",")
        
        orders.append(Order( item_name, item_quantity , item_variation ))

        logging.warn(f"Added item: {orders[i]}")
    logging.warn(f"Order: {orders}")
    return orders
