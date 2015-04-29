from replacement import System
import random
class Test:

    def __init__(self, system):
        self.system = system

    def select(self):
        self.system.query('customer',  random.randint(0, NUM_CUSTOMERS - 1), ['C_FNAME', 'C_LNAME'])

        self.system.query('item', random.randint(0, NUM_ITEMS - 1), ['key', 'I_THUMBNAIL'])
        self.system.query('item', random.randint(0, NUM_ITEMS - 1), ['key', 'I_THUMBNAIL'])

        self.system.query('item', random.randint(0, NUM_ITEMS - 1), ['key', 'i_title'])
        self.system.query('author', random.randint(0, NUM_AUTHORS), ['A_FNAME', 'A_LNAME'])

        self.system.query('author', random.randint(0, NUM_AUTHORS), []) #[] is for select *
        self.system.query('item', random.randint(0, NUM_ITEMS - 1), [])

        self.system.query('author', random.randint(0, NUM_AUTHORS), [])
        self.system.query('item', random.randint(0, NUM_ITEMS - 1), [])

        self.system.query('item', random.randint(0, NUM_ITEMS - 1), [])
        self.system.query('author', random.randint(0, NUM_AUTHORS), [])
        
        self.system.query('customer',  random.randint(0, NUM_CUSTOMERS - 1), ['C_UNAME'])
        
        self.system.query('customer',  random.randint(0, NUM_CUSTOMERS - 1), ['password'])

        self.system.query('customer',  random.randint(0, NUM_CUSTOMERS - 1), ['key'])

        self.system.query('orders',  random.randint(0, NUM_ORDERS - 1), [])
        self.system.query('customers',  random.randint(0, NUM_CUSTOMERS - 1), [])

        self.system.query('order_line',  random.randint(0, NUM_ORDERS_LINES - 1), [])
        #UNCERTAIN ON NUMBER!!!

        self.system.query('shopping_cart', str(random.randint(0, NUM_SHOPPING_CARTS)), [])
        #UNCERTAIN ON NUMBER!!!

        self.system.query('customer',  random.randint(0, NUM_CUSTOMERS - 1), ['C_DISCOUNT'])

        self.system.query('customer',  random.randint(0, NUM_CUSTOMERS - 1), ['c_ADDR_ID'])

        self.system.query('item', random.randint(0, NUM_ITEMS - 1), ['i_stock'])

        self.system.query('address', str(random.randint(0, NUM_ADDRESSES - 1)), ['ADDR_CO_ID'])

        self.system.query('country', str(random.randint(0, NUM_COUNTRIES - 1)), ['key'])
        #UNCERTAIN
        self.system.query('address', str(random.randint(0, NUM_ADDRESSES - 1)), ['ADDR_ID'])

        self.system.query('address', str(random.randint(0, NUM_ADDRESSES - 1)), ['ADDR_ID'])

        self.system.query('orders',  random.randint(0, NUM_ORDERS - 1), ['key'])
        
        self.system.query('shopping_cart', str(random.randint(0, NUM_SHOPPING_CARTS)), ['scl_qty'])
        #UNCERTAIN ON NUMBER

        self.system.query('shopping_cart', str(random.randint(0, NUM_SHOPPING_CARTS)), [])
        #UNCERTAIN
        self.system.query('shopping_cart', str(random.randint(0, NUM_SHOPPING_CARTS)), [])
        #UNCERTAIN

    def update(self):
        i = random.randint(0, NUM_ITEMS - 1)
        num = str(i)
        x = "'" + id + "'"
        date = "'" + "2014-08-03" + "'"
        self.system.update('item', num, {'I_COST': x, 'I_IMAGE': x, 'I_THUMBNAIL': x, 'I_PUB_DATE': date, 'I_RELATED1': str(i+1), 'I_RELATED2': str(i+2), 'I_RELATED3': str(i+3), 'I_RELATED4': str(i+4), 'I_RELATED5': str(i+5)})


        self.system.update('customer', str(random.randint(0, NUM_CUSTOMERS - 1)), {'C_LOGIN': "'" + "2014-03-04 01:00:00" + "'", 'C_EXPIRATION': "'" + "2014-03-04 01:00:00" + "'"})

        self.system.update('shopping_cart_line', str(random.randint(0, NUM_SHOPPING_CARTS)), {'scl_qty': str(1)})

        self.system.update('shopping_cart', str(random.randint(0, NUM_SHOPPING_CARTS)), {'sc_time': str(1)})


    def insert(self):
        self.system.insert('shopping_cart', {'skey': str(random.randint(0, NUM_SHOPPING_CARTS)), 'sc_time': str(1)})


        self.system.insert('customer', {'key': str(random.randint(0, NUM_CUSTOMERS)), 'C_UNAME': str(1), 'c_passwd': str(1), 'C_FNAME': str(1), 'C_LNAME': str(1), 'C_ADDR_ID': str(1), 'C_PHONE': str(1), 'C_EMAIL': str(1), 'C_SINCE': str(1), 'C_LAST_LOGIN': str(1), 'C_LOGIN': str(1), 'C_EXPIRATION': str(1), 'C_DISCOUNT': str(1), 'C_BALANCE': str(1), 'C_YTD_PMT': str(1), 'C_BIRTHDATE': str(1), 'C_DATA': str(1)})

        self.system.insert('order_line', {'cl_id': str(1), 'cl_key': str(1), 'cl_i_id': str(1), 'cl_qty': str(1), 'cl_discount': str(1), 'cl_comments': str(1)})

        self.system.insert('cc_xacts', {'key': str(1), 'CX_TYPE': str(1), 'CX_NUM': str(1), 'CX_NAME': str(1), 'CX_EXPIRE': str(1), 'CX_XACT_AMT': str(1), 'CX_XACT_DATE': str(1), 'CX_CO_ID': str(1)})


