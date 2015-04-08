import psycopg2
import sqlite3
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
