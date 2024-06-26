# Nuvembot

Nuvembot is a python software using selenium to get orders in the payment approved status but not shipped to the final consumer.
This bot get the order details, send to Whatsapp number via Selenium and print the shipping label. 


## Pre-req

First, you need the O.S Variables in your environment

`NUVEM_USER` - NUVEMSHOP USERNAME

`NUVEM_PASS` - NUVEMSHOP PASSWORD

`ADMIN_WHATSAPP` - WHATSAPP NUMBER TO RECEIVE NOTIFICATION

After that,you need install the requirements. Execute
```bash
pip install -r requirements.txt 
```

### PS
 You need to install FIREFOX and change in constants.py the binary and profile location. 
 You need to go in https://web.whatsapp.com and read the QRCODE to connect your Whatsapp.

## Running

To run the code, you can pass "pedidos" arg to execute the program in portuguese. To execute the program in English, remove the arg.

Portuguese:
```bash
python3 main.py pedidos
```
English:
```bash
python3 main.py pedidos
```

## Next Steps

In the supplier webpage, buy the products and sent to final consumer.

## Why are you dont use API ?

The nuvemshop and Whatsapp doesn't have a 100% free open API.  In Nuvemshop you need a few steps and the app will be list in App center - Its not my intention.

Whatsapp you need to register in Meta Developers and need switch the account to Whatsapp Business. 

In the Supplier, we don't have a API.

And the last and more important, I want to training more about the Selenium Automation.