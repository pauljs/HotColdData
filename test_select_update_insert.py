from replacement import System
import random

NUM_EBS = 10
NUM_ITEMS = 1000

NUM_CUSTOMERS = NUM_EBS * 2880 - 1
NUM_ADDRESSES = 2 * NUM_CUSTOMERS - 1
NUM_AUTHORS = NUM_ITEMS / 4  - 1
NUM_ORDERS = NUM_CUSTOMERS * 9 / 10 - 1 
NUM_COUNTRIES = 92 - 1

class Test:

    def __init__(self, system):
        self.system = system

    def select(self):
        #self.system.query('customer',  random.randint(0, NUM_CUSTOMERS - 1), ['C_FNAME', 'C_LNAME'])

        for i in range(0 , 1000):
            self.system.query('item', str(random.randint(0, 1)), ['key', 'I_THUMBNAIL'])
            self.system.query('item', str(random.randint(0, 1)), ['key', 'I_THUMBNAIL'])

            self.system.query('item', str(random.randint(0, 1)), ['key', 'i_title'])
            self.system.query('item', str(random.randint(0, 1)), [])
        #self.system.query('author', str(random.randint(0, NUM_AUTHORS)), ['A_FNAME', 'A_LNAME'])

        #self.system.query('author', str(random.randint(0, NUM_AUTHORS)), []) #[] is for select *

        #self.system.query('author', str(random.randint(0, NUM_AUTHORS)), [])
            #self.system.query('item', str(random.randint(0, NUM_ITEMS - 1)), [])

            #self.system.query('item', str(random.randint(0, NUM_ITEMS - 1)), [])
        #self.system.query('author', str(random.randint(0, NUM_AUTHORS)), [])
        
#        self.system.query('customer',  str(random.randint(0, NUM_CUSTOMERS - 1)), ['C_UNAME'])
        
#        self.system.query('customer',  str(random.randint(0, NUM_CUSTOMERS - 1)), ['C_PASSSWD'])

#        self.system.query('customer',  str(random.randint(0, NUM_CUSTOMERS - 1)), ['key'])

        #self.system.query('orders',  str(random.randint(0, NUM_ORDERS - 1)), [])
#        self.system.query('customer',  str(random.randint(0, NUM_CUSTOMERS - 1)), [])

        #self.system.query('order_line',  str(random.randint(0, NUM_ORDERS - 1)), [])
        #UNCERTAIN ON NUMBER!!!

        #self.system.query('shopping_cart', str(random.randint(0, NUM_ORDERS - 1)), [])
        #UNCERTAIN ON NUMBER!!!

#        self.system.query('customer',  str(random.randint(0, NUM_CUSTOMERS - 1)), ['C_DISCOUNT'])

#        self.system.query('customer',  str(random.randint(0, NUM_CUSTOMERS - 1)), ['C_ADDR_ID'])

        #self.system.query('item', str(random.randint(0, NUM_ITEMS - 1)), ['I_STOCK'])

        #self.system.query('address', str(random.randint(0, NUM_ADDRESSES - 1)), ['ADDR_CO_ID'])

        #self.system.query('country', str(random.randint(0, NUM_COUNTRIES - 1)), ['key'])
        #UNCERTAIN
        #self.system.query('address', str(random.randint(0, NUM_ADDRESSES - 1)), ['key'])

        #self.system.query('address', str(random.randint(0, NUM_ADDRESSES - 1)), ['key'])

        #self.system.query('orders',  str(random.randint(0, NUM_ORDERS - 1)), ['key'])
        
        #self.system.query('shopping_cart_line', str(random.randint(0, NUM_ORDERS - 1)), ['SCL_QTY'])
        #UNCERTAIN ON NUMBER

        #self.system.query('shopping_cart', str(random.randint(0, NUM_ORDERS - 1)), [])
        #UNCERTAIN
        #self.system.query('shopping_cart', str(random.randint(0, NUM_ORDERS - 1)), [])
        #UNCERTAIN

    def update(self):
        i = random.randint(0, NUM_ITEMS - 1)
        num = str(i)
        x = "'" + num + "'"
        date = "'" + "2014-08-03" + "'"
        self.system.update('item', num, {'I_COST': x, 'I_IMAGE': x, 'I_THUMBNAIL': x, 'I_PUB_DATE': date, 'I_RELATED1': str(i+1), 'I_RELATED2': str(i+2), 'I_RELATED3': str(i+3), 'I_RELATED4': str(i+4), 'I_RELATED5': str(i+5)})


        #self.system.update('customer', str(random.randint(0, NUM_CUSTOMERS - 1)), {'C_LOGIN': "'" + "2014-03-04 01:00:00" + "'", 'C_EXPIRATION': "'" + "2014-03-04 01:00:00" + "'"})

        i = random.randint(0, NUM_ORDERS - 1)
        timestamp = "'" + "2014-04-05 01:00:00" + "'"
        self.system.update('shopping_cart_line', str(random.randint(0, NUM_ORDERS - 1)), {'SCL_QTY': str(i)})

        self.system.update('shopping_cart', str(random.randint(0, NUM_ORDERS - 1)), {'SC_TIME': timestamp})


    def insert(self):
        i = random.randint(0, NUM_ITEMS - 1)
        date = "'" + "2014-04-05" + "'"
        timestamp = "'" + "2014-04-05 01:00:00" + "'"
        self.system.insert('shopping_cart', {'key': str(i), 'SC_TIME': timestamp})


        #self.system.insert('customer', {'key': str(random.randint(0, NUM_CUSTOMERS)), 'C_UNAME': str(1), 'C_PASSWD': str(1), 'C_FNAME': str(1), 'C_LNAME': str(1), 'C_ADDR_ID': str(1), 'C_PHONE': str(1), 'C_EMAIL': str(1), 'C_SINCE': date, 'C_LAST_LOGIN': date, 'C_LOGIN': timestamp, 'C_EXPIRATION': timestamp, 'C_DISCOUNT': str(1), 'C_BALANCE': str(1), 'C_YTD_PMT': str(1), 'C_BIRTHDATE': date, 'C_DATA': str(1)})

        i = random.randint(0, NUM_ORDERS - 1)
        num = str(i)
        x = "'" + num + "'"
        self.system.insert('order_line', {'key': num, 'OL_O_ID': num, 'OL_I_ID': num, 'OL_QTY': num, 'OL_DISCOUNT': num, 'OL_COMMENTS': x})

        #self.system.insert('cc_xacts', {'key': str(1), 'CX_TYPE': str(1), 'CX_NUM': str(1), 'CX_NAME': str(1), 'CX_EXPIRE': date, 'CX_XACT_AMT': str(1), 'CX_XACT_DATE': str(1), 'CX_CO_ID': str(1)})
