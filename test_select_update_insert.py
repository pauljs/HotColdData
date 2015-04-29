from replacement import System
import random
class Test:

    def __init__(self, system):
        self.system = system

    def select(self):
        self.system.query('customer',  random.randint(0, NUM_CUSTOMERS - 1), [c_fname, c_lname])

        self.system.query('item', random.randint(0, NUM_ITEMS - 1), [i_id, i_thumbnail])
        self.system.query('item', random.randint(0, NUM_ITEMS - 1), [i_id, i_thumbnail])

        self.system.query('item', random.randint(0, NUM_ITEMS - 1), [i_id, i_title])
        self.system.query('author', random.randint(0, NUM_AUTHORS), [a_fname, a_lname])

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

        self.system.query('order_line',  random.randint(0, NUM_ORDERS - 1), [])

