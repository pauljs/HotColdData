from replacement import System
import random
class Test:

    def __init__(self, system):
        self.system = system

    def select(self):
        self.system.query('customer',  random.randint(0, NUM_CUSTOMERS - 1), ['c_fname', 'c_lname'])

        self.system.query('item', random.randint(0, NUM_ITEMS - 1), ['i_id', 'i_thumbnail'])
        self.system.query('item', random.randint(0, NUM_ITEMS - 1), ['i_id', 'i_thumbnail'])

        self.system.query('item', random.randint(0, NUM_ITEMS - 1), ['i_id', 'i_title'])
        self.system.query('author', random.randint(0, NUM_AUTHORS), ['a_fname', 'a_lname'])

        self.system.query('author', random.randint(0, NUM_AUTHORS), []) #[] is for select *
        self.system.query('item', random.randint(0, NUM_ITEMS - 1), [])

        self.system.query('author', random.randint(0, NUM_AUTHORS), [])
        self.system.query('item', random.randint(0, NUM_ITEMS - 1), [])

        self.system.query('item', random.randint(0, NUM_ITEMS - 1), [])
        self.system.query('author', random.randint(0, NUM_AUTHORS), [])
        
        self.system.query('customer',  random.randint(0, NUM_CUSTOMERS - 1), ['c_uname'])
        
        self.system.query('customer',  random.randint(0, NUM_CUSTOMERS - 1), ['password'])

        self.system.query('customer',  random.randint(0, NUM_CUSTOMERS - 1), ['c_id'])

        self.system.query('orders',  random.randint(0, NUM_ORDERS - 1), [])
        self.system.query('customers',  random.randint(0, NUM_CUSTOMERS - 1), [])

        self.system.query('order_line',  random.randint(0, NUM_ORDERS_LINES - 1), [])
        #UNCERTAIN ON NUMBER!!!

        self.system.query('shopping_cart', str(random.randint(0, NUM_SHOPPING_CARTS)), [])
        #UNCERTAIN ON NUMBER!!!

        self.system.query('customer',  random.randint(0, NUM_CUSTOMERS - 1), ['c_discount'])

        self.system.query('customer',  random.randint(0, NUM_CUSTOMERS - 1), ['c_addr_id'])

        self.system.query('item', random.randint(0, NUM_ITEMS - 1), ['i_stock'])

        self.system.query('address', str(random.randint(0, NUM_ADDRESSES - 1)), ['addr_co_id'])

        self.system.query('country', str(random.randint(0, NUM_COUNTRIES - 1)), ['co_id'])
        #UNCERTAIN
        self.system.query('address', str(random.randint(0, NUM_ADDRESSES - 1)), ['addr_id'])

        self.system.query('address', str(random.randint(0, NUM_ADDRESSES - 1)), ['addr_id'])

        self.system.query('orders',  random.randint(0, NUM_ORDERS - 1), ['c_id'])
        
        self.system.query('shopping_cart', str(random.randint(0, NUM_SHOPPING_CARTS)), ['scl_qty'])
        #UNCERTAIN ON NUMBER

        self.system.query('shopping_cart', str(random.randint(0, NUM_SHOPPING_CARTS)), [])
        #UNCERTAIN
        self.system.query('shopping_cart', str(random.randint(0, NUM_SHOPPING_CARTS)), [])
        #UNCERTAIN

    def update(self):
        self.system.update('item', str(random.randint(0, NUM_ITEMS - 1)), {'i_cost': str(random.randint(1, 100)), 'i_image': str(random.randint(1, 100)), 'i_thumbnail': str(randomrandint(1, 100)), 'i_pub_date': str(randomrantint(1, 100)), 'i_related1': str(randomrantint(1, 100)), 'i_related': str(randomrantint(1, 100)), 'i_related3': str(randomrantint(1, 100)), 'i_related4': str(randomrantint(1, 100)), 'i_related5': str(randomrantint(1, 100))})

        self.system.update('customer', str(random.randint(0, NUM_CUSTOMERS - 1)), {'c_login': str(randomrantint(1, 100)), 'c_expiration': str(randomrantint(1, 100))})

        self.system.update('shopping_cart_line', str(random.randint(0, NUM_SHOPPING_CARTS)), {'scl_qty': str(1)})

        self.system.update('shopping_cart', str(random.randint(0, NUM_SHOPPING_CARTS)), {'sc_time': str(1)})


    def insert(self):
        self.system.insert('shopping_cart', {'sc_id': str(random.randint(0, NUM_SHOPPING_CARTS)), 'sc_time': str(1)})


        self.system.insert('customer', {'c_id': str(random.randint(0, NUM_CUSTOMERS)), 'c_uname': str(1), 'c_passwd': str(1), 'c_fname': str(1), 'c_lname': str(1), 'c_addr_id': str(1), 'c_phone': str(1), 'c_email': str(1), 'c_since': str(1), 'c_last_login': str(1), 'c_login': str(1), 'c_expiration': str(1), 'c_discount': str(1), 'c_balance': str(1), 'c_ytd_pmt': str(1), 'c_birthdate': str(1), 'c_data': str(1)})

        self.system.insert('order_line', {'cl_id': str(1), 'cl_c_id': str(1), 'cl_i_id': str(1), 'cl_qty': str(1), 'cl_discount': str(1), 'cl_comments': str(1)})

        self.system.insert('cc_xacts', {'cx_c_id': str(1), 'cx_type': str(1), 'cx_num': str(1), 'cx_name': str(1), 'cx_expire': str(1), 'cx_xact_amt': str(1), 'cx_xact_date': str(1), 'cx_co_id': str(1)})


