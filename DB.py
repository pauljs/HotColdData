import psycopg2
import sqlite3
import memcache
import happybase

DB_NAME = 'hot_cold_data'

class DB:
    def __init__(self, db_name):
        try:
            self.conn = psycopg2.connect("dbname='%s'" % db_name)
        except:
            print "I am unable to connect to the database"
            exit()
        self.cur = self.conn.cursor()

    def cursor(self):
        return self.cur

    def getNewCursor(self):
        return self.conn.cursor()

    def connection(self):
        return self.conn

    def delete(self, table, key):
        self.cur.execute("delete from " + table + " where key = " + key + ";")

    def commit(self):
        self.conn.commit()

    def insert(self, table, data):
        q = "insert into " + table + " VALUES ("
        for d in data:
            q += data[d] + ' ,'
        q = q[:len(q)-1] + ');'
        self.cur.execute(q)

    def select(self, table, key, cols):
        q = 'Select '
        for c in cols:
            q += c + ','
        q = q[:len(q) - 1] + ' from ' + table + ' where key = ' + key + ';'
        return self.query(q)

    def update(self, table, key, data):
        q = 'UPDATE ' + table + ' set '
        for d in data:
            q  += d + ' = ' + data[d] + ','
        q = q[:len(q) - 1] + ' where key = ' + key + ';'
        self.cur.execute(q)

    def query(self, q):
        self.cur.execute(q)
        return self.cur.fetchall()


'''
Tutorial:
https://happybase.readthedocs.org/en/happybase-0.4/tutorial.html
'''
class Hbase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = happybase.Connection('hadoop-node2.vampire', table_prefix=db_name)

    def get_connection(self):
        return self.connection	

    def get_tables(self):
        return self.connection.tables()

    def table(self, table):
        return self.connection.table(table)
    
    def insert(self, table, key, data):
        dict = {}
        for d in data:
            dict['default:' + d] = data[d]
        self.table(table).put(str(key), dict)

    def update(self, table, key, data):
        self.insert(table, key, data)

    def delete(self, key):
        self.table(table).delete(key)
