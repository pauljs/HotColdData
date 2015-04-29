from replacement import System
import sys


NUM_EBS = 10
NUM_ITEMS = 1000

NUM_CUSTOMERS = NUM_EBS * 2880
NUM_ADDRESSES = 2 * NUM_CUSTOMERS
NUM_AUTHORS = NUM_ITEMS / 4
NUM_ORDERS = NUM_CUSTOMERS * 9 / 10


def createTables(s):
    print 'creating tables'

    s.initialize('address', {'key': 'bigint', 'ADDR_STREET1': 'varchar(40)', 'ADDR_STREET2': 'varchar(40)', 'ADDR_CITY': 'varchar(30)', 'ADDR_STATE': 'varchar(20)', 'ADDR_ZIP': 'varchar(10)', 'ADDR_CO_ID': 'bigint'})

    s.initialize('author', {'key': 'bigint', 'A_FNAME': 'varchar(20)', 'A_LNAME': 'varchar(20)', 'A_MNAME': 'varchar(20)', 'A_DOB': 'date', 'A_BIO': 'varchar(280)'})

    s.initialize('country', {'key': 'bigint', 'CO_NAME': 'varchar(50)', 'CO_EXCHANGE': 'bigint', 'CO_CURRENCY': 'varchar(18)'})
    
    s.initialize('customer', {'key': 'bigint', 'C_UNAME': 'varchar(20)', 'c_PASSSWD': 'varchar(20)', 'C_FNAME': 'varchar(17)', 'c_LNAME': 'varchar(17)', 'C_ADDR_ID': 'bigint', 'C_PHONE': 'varchar(18)', 'C_EMAIL': 'varchar(50)', 'C_SINCE': 'date', 'C_LAST_LOGIN': 'date', 'C_LOGIN': 'timestamp', 'C_EXPIRATION': 'timestamp', 'C_DISCOUNT': 'real', 'C_BALANCE': 'bigint', 'C_YTD_PMT': 'bigint', 'C_BIRTHDATE': 'date', 'c_DATA': 'varchar(510)'})

    s.initialize('item', {'key': 'bigint', 'I_TITLE': 'varchar(60)', 'I_A_ID': 'bigint', 'I_PUB_DATE': 'date', 'I_PUBLISHER': 'varchar(60)', 'I_SUBJECT': 'varchar(60)', 'I_DESC': 'varchar(280)', 'I_RELATED1': 'bigint', 'I_RELATED2': 'bigint', 'I_RELATED3': 'bigint', 'I_RELATED4': 'bigint', 'I_RELATED5': 'bigint', 'I_THUMBNAIL': 'varchar(40)', 'I_IMAGE': 'varchar(40)', 'I_SRP': 'bigint', 'I_COST': 'bigint', 'I_AVAIL': 'date', 'I_STOCK': 'bigint', 'I_ISBN': 'varchar(13)', 'I_PAGE':'bigint', 'I_BACKING': 'varchar(15)', 'I_DIMENSTIONS': 'varchar(25)'})

    s.initialize('cc_xacts', {'key': 'bigint', 'CX_TYPE': 'varchar(10)', 'CX_NUM': 'varchar(20)', 'CX_NAME': 'varchar(30)', 'CX_EXPIRE': 'date', 'CX_AUTH_ID': 'varchar(15)', 'CX_XACT_AMT': 'bigint', 'CX_XACT_DATE': 'date', 'CX_CO_ID': 'bigint'})

    s.initialize('order_line', {'key': 'bigint', 'OL_O_ID': 'bigint', 'OL_I_ID': 'bigint', 'OL_QTY': 'bigint', 'OL_DISCOUNT': 'bigint', 'OL_COMMENTS': 'varchar(110)'})

    s.initialize('orders', {'key': 'bigint', 'O_C_ID': 'bigint', 'O_DATE': 'date', 'O_SUB_TOTAL': 'bigint', 'O_TAX': 'bigint', 'O_TOTAL': 'bigint', 'O_SHIP_TYPE': 'varchar(10)', 'O_SHIP_DATE': 'date', 'O_BILL_ADDR_ID': 'bigint', 'O_SHIP_ADDR_ID': 'bigint', 'O_STATUS': 'varchar(15)'})

    s.initialize('shopping_cart', {'key': 'bigint', 'SC_TIME': 'timestamp'})

    s.initialize('shopping_cart_line', {'key': 'bigint', 'SCL_QTY': 'bigint', 'SCL_I_ID': 'bigint'})

    print 'done'

def populateAddressTable(s):
    print 'Popualting Address Table' 
    l = []
    for i in xrange(0,NUM_ADDRESSES):
        num = str(i)
        x = "'" + num + "'"
        l.append({'key': num, 'ADDR_STREET1': x, 'ADDR_STREET2': x, 'ADDR_CITY': x, 'ADDR_STATE': x, 'ADDR_ZIP': x, 'ADDR_CO_ID': num})
        if i % 15017 == 0:
            sys.stdout.write('.')
            sys.stdout.flush()
    s.load('address', l)
    print 'done'

def populateAuthorTable(s):
    print 'Populating Author Table'
    l = []
    for i in xrange(0,NUM_AUTHORS):
        num = str(i)
        x = "'" + num + "'"
        date = "'" + "2014-03-04" "'"
        l.append({'key': num, 'A_FNAME': x, 'A_LNAME': x, 'A_MNAME': x, 'A_DOB': date, 'A_BIO': x})
    s.load('author', l)
    print 'done'
        
def populateCountryTable(s):
    print 'Populating Country Table'
    l = []
    for i in xrange(0,92):
        num = str(i)
        x = "'" + num + "'"
        l.append({'key': num, 'CO_NAME': x, 'CO_EXCHANGE': num, 'CO_CURRENCY': x})
    s.load('country', l)
    print 'done'

def populateCustomerTable(s):
    print 'populating customer table'
    l = []
    for i in xrange(0,NUM_CUSTOMERS):
        num = str(i)
        x = "'" + num + "'"
        date = "'" + "2014-03-04" + "'"
        timestamp = "'" + "2014-03-04 01:00:00" + "'"
        l.append({'key': num, 'C_UNAME': x, 'c_PASSSWD': x, 'C_FNAME': x, 'c_LNAME': x, 'C_ADDR_ID': num, 'C_PHONE': x, 'C_EMAIL': x, 'C_SINCE': date, 'C_LAST_LOGIN': date, 'C_LOGIN': timestamp, 'C_EXPIRATION': timestamp, 'C_DISCOUNT': num, 'C_BALANCE': num, 'C_YTD_PMT': num, 'C_BIRTHDATE': date, 'c_DATA': x})
    s.load('customer', l)
    print 'done'

def populateItemTable(s):
    print 'populating item table'
    l = []
    for i in xrange(0,NUM_ITEMS):
        num = str(i)
        x = "'" + num + "'"
        date = "'" + "2014-08-03" + "'"
        l.append({'key': num, 'I_TITLE': x, 'I_A_ID': num, 'I_PUB_DATE': date, 'I_PUBLISHER': x, 'I_SUBJECT': x, 'I_DESC': x, 'I_RELATED1': str(i+1), 'I_RELATED2': str(i+2), 'I_RELATED3': str(i+3), 'I_RELATED4': str(i+4), 'I_RELATED5': str(i+5), 'I_THUMBNAIL': x, 'I_IMAGE': x, 'I_SRP': num, 'I_COST': num, 'I_AVAIL': date, 'I_STOCK': num, 'I_ISBN': x, 'I_PAGE': num, 'I_BACKING': x, 'I_DIMENSTIONS': x})
    s.load('item', l)
    print 'done'

def populateCC_XACTSAndOrders(s):
    print 'populating orders, transactions and shopping cart'
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    for i in xrange(0,NUM_ORDERS):
        num = str(i)
        x = "'" + num + "'"
        date = "'" + "2014-04-05" + "'"
        timestamp = "'" + "2014-04-05 01:00:00" + "'"
        l1.append({'key': num, 'CX_TYPE': x, 'CX_NUM': x, 'CX_NAME': x, 'CX_EXPIRE': date, 'CX_AUTH_ID': x, 'CX_XACT_AMT': num, 'CX_XACT_DATE': date, 'CX_CO_ID': num})

        l2.append({'key': num, 'OL_O_ID': num, 'OL_I_ID': num, 'OL_QTY': num, 'OL_DISCOUNT': num, 'OL_COMMENTS': x})

        l3.append({'key': num, 'O_C_ID': num, 'O_DATE': date, 'O_SUB_TOTAL': num, 'O_TAX': num, 'O_TOTAL': num, 'O_SHIP_TYPE': x, 'O_SHIP_DATE': date, 'O_BILL_ADDR_ID': num, 'O_SHIP_ADDR_ID': num, 'O_STATUS': x})

        l4.append({'key': num, 'SC_TIME': timestamp})

        l5.append({'key': num, 'SCL_QTY': num, 'SCL_I_ID': num})
    s.load('cc_xacts', l1)
    s.load('order_line', l2)
    s.load('orders', l3)
    s.load('shopping_cart', l4)
    s.load('shopping_cart_line', l5)
    print 'done'


def main():
    print 'Beginning TPCW Database Population.'
    s = System()
    s.setReplacementAlgorithm('LRU', 1000)
    createTables(s)
    populateAddressTable(s)
    populateAuthorTable(s)
    populateCountryTable(s)
    populateCustomerTable(s)
    populateItemTable(s)
    populateCC_XACTSAndOrders(s)
    print 'Fine'

if __name__ == '__main__':
    main()

