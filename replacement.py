import happybase
import json
from DB import DB, DB_NAME, Hbase
from LRUQueue import LRUQueue


class System:
    def __init__(self):
        self.hot = DB(DB_NAME)
        self.cold = Hbase(DB_NAME)

    def initialize(self, name, cols):
        try:
            self.cold.get_connection().create_table(name, {'default':dict()})
        except happybase.hbase.ttypes.AlreadyExists:
            pass
        self.hot.cursor().execute("drop table if exists " + name + ";")
        create_table = "create table " + name + "("
        for key in cols:
            create_table += key + " " + cols[key] + ","
        create_table = create_table[:len(create_table) -1] + ");"
        self.hot.cursor().execute(create_table)
        self.hot.connection().commit()

    def load(self):
        pass

    def setReplacementAlgorithm(self, name, size):
        if name == 'LRU':
            self.replacement_algorithm = LRUQueue(size)
    
    def insert(self, table, data):
        val = self.replacement_algorithm.enqueueLRU(data['key'])
        if val != -1:
            self.hot.cursor().execute("delete from " + table + " where key = " + str(val) + ";")
        query = "insert into " + table + " VALUES ("
        for d in data:
            query += data[d] + " ,"
        query = query[:len(query)-1] + ");"
        self.hot.cursor().execute(query)
        self.hot.connection().commit()
        dict = {}
        for key in data:
            dict['default:' + key] = data[key]
        self.cold.table(table).put(str(data['key']), dict)
	

    #TODO error conditions
    def query(self, table, key, cols):
        if not self.replacement_algorithm.contains(key):
            val = self.replacement_algorithm.enqueueLRU(key)
            if val != -1:
                self.hot.cursor().execute("delete from " + table + " where key = " + val + ";")
            data = self.cold.table(table).row(key)
            query = "insert into " + table + " VALUES ("
            for d in data:
                query += data[d] + " ,"
            query = query[:len(query)-1] + ");"
            self.hot.cursor().execute(query)
            self.hot.connection().commit()
        select = "SELECT " 
        for c in cols:
            select += c + ","
        select = select[:len(select)-1] + " from " + table  + " where key = " + key
        return self.hot.query(select)

    def delete(self, table, key):
        if self.replacement_algorithm.delete(key):
            hot.cursor().execute("DELETE from " + table + " where key = " + key + ";")
        cold.table(table).delete(key)

    def update(self, table, key, data):
        if self.replacement_algorithm.contains(key):
            query = "UPDATE " + table + " set " 
            for d in data:
                query += d + " = " + data[d] + ","
            query = query[:len(query)-1] + " where key = " + key + ";"
            self.hot.cursor().execute(query)
            self.hot.connection().commit()

def main():
    s = System()
    s.setReplacementAlgorithm('LRU', 10)
    s.initialize("test", {'key': 'bigint', 'text': 'varchar(280)'})
    for i in range(0,20):
        s.insert('test', {'key': str(i), 'text': "'helloworld'"})
    print s.query('test', '5', ['key', 'text'])
    s.delete('test', '5')



if __name__ == '__main__':
    main()
