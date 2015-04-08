import happybase
import json
from DB import DB, DB_NAME, Hbase
from LRUQueue import LRUQueue

class MyHbase:
    def __init__(self):
        self.hbase = Hbase(DB_NAME)
    def add(self, key, item):
        pass        

class MyDB:
    def __init__(self):
        self.db = DB(DB_NAME)
    

class System:
    def __init__(self):
        self.hot = DB(DB_NAME)
        self.cold = Hbase(DB_NAME)

        try:
            self.cold.get_connection().create_table('twitter', {'default':dict({})})
        except happybase.hbase.ttypes.AlreadyExists:
            pass
        self.hot.cursor().execute("drop table if exists twitter")
        self.hot.cursor().execute("create table twitter(id bigint, text varchar(280))")
        self.hot.connection().commit()

    def setReplacementAlgorithm(self, name):
        if name == 'LRU':
            self.replacement_algorithm = LRUQueue(10)
    
    def insert(self, table, key, data):
        val = self.replacement_algorithm.enqueueLRU(key)
        if val != -1:
            self.hot.cursor().execute("delete from " + table + " where id = " + str(val) + ";")
        self.hot.cursor().execute("insert into " + table  + " VALUES (%s, %s)", (key, data))
        self.hot.connection().commit()
        self.cold.table(table).put(str(key), {'default:data' : data.encode('utf-8').strip()})


    #TODO error conditions
    def query(self, table, key):
        if not self.replacement_algorithm.contains(key):
            val = self.replacement_algorithm.enqueueLRU(key)
            if val != -1:
                self.hot.cursor().execute("delete from " + table + " where id = " + val + ";")
            data = self.cold.table(table).row(key)['default:data']
            self.hot.cursor().execute("insert into %s VALUES (%s, %s)", (table, key, data))
        
        self.hot.connection().commit()
        hot.cursor().execute("Select * from %s where id = %s", (table, key))
        return hot.cursor().fetchall()

    def delete(self, table, key):
        if self.replacement_algorithm.contains(key):
            self.replacement_algorithm.delete(key)
            hot.cursor().execute("delete from %s where id = %s", (table, key))
        cold.table(table).delete(key)

    def update(self, table, key, data):
        pass
        #need to think on this to be efficient

def main():
    s = System()
    s.setReplacementAlgorithm('LRU')
    tweets = []
    for line in open('tweets_1k.json'):
        try:
            tweets.append(json.loads(line))
        except:
            pass
    for t in tweets:
        s.insert('twitter', t['id'], t['text'])
        #print s.hot.query("select * from twitter")

    

if __name__ == '__main__':
    main()
