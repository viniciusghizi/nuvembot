import os

#ETC
GRAPHIC_INTERFACE=1

#NUVEMSHOP

USER_NUVEMSHOP = os.getenv("NUVEM_USER")
PASS_NUVEMSHOP = os.getenv("NUVEM_PW")
URL_NUVEMSHOP ='https://xpecial.lojavirtualnuvem.com.br/admin/v2/dashboard/'
URL_CONFIRMED_PAYMENT = 'https://xpecial.lojavirtualnuvem.com.br/admin/v2/orders?page=1&perPage=50&fulfillmentStatus=unpacked&paymentStatus=paid'


#SUPPLIER
USER_SUPPLIER = ""
PASS_SUPPLIER = ""
URL_SUPPLIER=os.getenv('URL_SUPPLIER')
GRAPHIC_INTERFACE = 1

#WHATSAPP
PHONE = os.getenv('ADMIN_WHATSAPP')
PHONE_MAGIE_BANK = os.getenv('BANK_WHATSAPP') 
MESSAGE_ORDER_CHECKED = 'NOVO PEDIDO LOCALIZADO'
MESSAGE_ORDER_SENDED = 'Write the message here'
MESSAGE_ORDER_NOT_FOUNDED = "NÃO HÁ NOVO PEDIDO"

#ELEMENTS WHATSAPP

X_SEND_MESSAGE_BUTTON = '/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'

#ELEMENTS NUVEM
ID_USER_NUVEM = 'user-mail'
ID_PASS_NUVEM = 'pass'
ID_SEARCH_NUVEM = 'input_search'
X_HOME_NUVEM = '/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/h1'
X_PRINT_BUTTON = '/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[3]/div/button'
X_PRODUCTS_QUANTITY = '/html/body/div[1]/div/div[2]/div[2]/div/div/div[4]/div/main/section[1]/div/div[2]/div[1]/div/h4'
X_PDF_PRINT = '/html/body/div[6]/div[2]/div[3]/div[4]/div[3]/button'

X_ORDER_NUMBER = '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div/a'
X_EMBALADO_BUTTON = '/html/body/div[1]/div/div[2]/div[2]/div/div/div[4]/div/main/section[1]/div/div[4]/div[3]/div/div/button'
X_ORDER_DETAIL_NAME = '/html/body/div[1]/div/div[2]/div[2]/div/div/div[4]/div/main/section[1]/div/div[2]/div[2]/div/div/div[#]/div[1]/div/div/div[2]/div/div/div[1]/a/p'
X_ORDER_DETAIL_VARIATION = '/html/body/div[1]/div/div[2]/div[2]/div/div/div[4]/div/main/section[1]/div/div[2]/div[2]/div/div/div[#]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/p'
X_ORDER_DETAIL_QUANTITY = '/html/body/div[1]/div/div[2]/div[2]/div/div/div[4]/div/main/section[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[3]/p'

#ELEMENTS SUPPLIER
X_HOME_SUPPLIER = ''
