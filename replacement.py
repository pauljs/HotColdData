import happybase
import json
from DB import DB, DB_NAME, Hbase
from LRUQueue import LRUQueue

class MyHbase:
    def __init__(self):
        self.hbase = Hbase(DB_NAME)
    #def add(self, key, item):
        

class MyDB:
    def __init__(self):
        self.db = DB(DB_NAME)
    

class System:
    def __init__(self):
        self.hot = DB(DB_NAME)
        self.cold = Hbase(DB_NAME)

        try:
            self.cold.get_connection().create_table('twitter', {'default':dict()})
        except happybase.hbase.ttypes.AlreadyExists:
            pass
        self.hot.cursor().execute("drop table if exists twitter")
        self.hot.cursor().execute("create table twitter(id bigint, text varchar(280))")
        self.hot.connection().commit()

    def load(self):
        for line in open('../tweets_1k.json'):
            #try:        
                t = json.loads(line)
                id = t['id']
                tweet = t['text'].encode('utf-8').strip()
                self.insert('twitter', id, tweet)
            #except:
                #print("Error loading table")
                #pass

    def setReplacementAlgorithm(self, name):
        if name == 'LRU':
            #arbitrarily picked the size of 20 for the LRUQueue maxsize
            self.replacement_algorithm = LRUQueue(20)
    
    def insert(self, table, key, data):
        val = self.replacement_algorithm.enqueueLRU(key)
        if val != -1:
            self.hot.query("delete from %s where id = %s" % (table, val))
        self.hot.query("insert into %s VALUES (%s, \"%s\")" % (table, key, data))
        self.cold.table(table).put(key, {'default:data' : data})
	


    #TODO error conditions
    def query(self, table, key):
        if not self.replacement_algorithm.contains(key):
            val = self.replacement_algorithm.enqueueLRU(key)
            if val != -1:
                self.hot.query("delete from %s where id = %s" % (table, val))
            data = self.cold.table(table).row(key)['default:data']
            self.hot.query("insert into %s VALUES (%s, \"%s\")" % (table, key, data))

        return self.hot.query("Select * from %s where id = %s" % (table, key))


    def delete(self, table, key):
        if self.replacement_algorithm.contains(key):
            self.replacement_algorithm.delete(key)
            hot.query("delete from %s where id = %s", table, key)
        cold.table(table).delete(key)

    def update(self, table, key, data):
        pass
        #need to think on this to be efficient

def main():
    s = System()
    s.setReplacementAlgorithm('LRU')

    #load in the tweets from tweets_1k
    s.load()

    print "query result:"
    print s.query('twitter',491122195247005697)

    '''
    tweets = []
    for line in open('tweets_1k.json'):
        try:
            tweets.append(json.loads(line))
        except:
            pass
    '''

def test_test():
    s = System()
    s.setReplacementAlgorithm('LRU')
    
    #load in the tweets from tweets_1k
    s.load()

    

    
    assert 1==2

if __name__ == '__main__':
    main()
