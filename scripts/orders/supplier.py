from pyshadow.main import Shadow
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging

from classes.supplier_class import supplier_class as Supplier
from classes.order_class import order_class as Order
from scripts.login import login
from messages import messages as Messages

def create_order_supplier(driver: WebDriver, nuvemshop_order):
    return print("not implemented yet")

def upload_order(driver: WebDriver, supplier: Supplier):
    return print("not implemented yet")

def buy_itens(driver: WebDriver, order: Order):
    return print("not implemented yet")