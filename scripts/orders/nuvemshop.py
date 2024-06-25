
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from classes.order_class import order_class as Order
import logging, time

from variables.constants import URL_NUVEMSHOP,ID_USER_NUVEM, ID_PASS_NUVEM, USER_NUVEMSHOP,PASS_NUVEMSHOP,URL_CONFIRMED_PAYMENT, X_ORDER_NUMBER, X_ORDER_DETAIL_NAME, X_ORDER_DETAIL_VARIATION, X_ORDER_DETAIL_QUANTITY, X_EMBALADO_BUTTON, X_PRODUCTS_QUANTITY, MESSAGE_ORDER_CHECKED, MESSAGE_ORDER_NOT_FOUNDED
from scripts.login import login
from scripts.utils.notifications import whatsapp_notification as NotificationService
from messages import messages as Messages


def check_created_orders(driver: WebDriver, message: Messages) :
    
    driver.get(URL_NUVEMSHOP)
    logging.warning(message['WARN_NUVEMSHOP_LOGIN'])
    
    login( ID_USER_NUVEM , ID_PASS_NUVEM , USER_NUVEMSHOP , PASS_NUVEMSHOP ,  driver )

    orders = get_order( driver, message )

    if len(orders) > 0:
        print_order( driver, message )
        NotificationService.whatsapp_notification( driver , MESSAGE_ORDER_CHECKED, message )
        NotificationService.whatsapp_notification( driver , orders, message )
    
    else :
        NotificationService.whatsapp_notification( driver, MESSAGE_ORDER_NOT_FOUNDED, message )

def print_order(driver: WebDriver, message: Messages) :
    url = driver.current_url 
    driver.get(url.replace("v2/orders/","orders/packing_slip/"))

    logging.warning(message['WARN_NUVEMSHOP_PRINTING_ORDER'])
    driver.execute_script("window.print()")
    
    logging.warning(message['WARN_NUVEMSHOP_PRINTED_ORDER'])

def update_order(driver: WebDriver) :
    return driver.find_element(By.XPATH, X_EMBALADO_BUTTON).click()

def get_order(driver: WebDriver, message: Messages):
    driver.get(URL_CONFIRMED_PAYMENT)
    logging.warning(message['WARN_NUVEMSHOP_GET_ORDER'])
    
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

        logging.warn(f"{message['WARN_NUVEMSHOP_ADDED_ITEM']} {orders[i]}")
    logging.warn(f" {message['INFO_NUVEMSHOP_ORDER']} {orders}")
    return orders
