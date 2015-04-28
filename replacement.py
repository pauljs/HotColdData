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
        elif name == 'FIFO':
            self.replacement_algorithm = FIFOQueue(size)
        elif name == 'CLOCK1':
            self.replacement_algorithm = ClockStaticQueue(size)
        elif name == 'CLOCK2':
            self.replacement_algorithm = ClockDynamicQueue(size)
        elif name == 'RANDOM':
            self.replacement_algorithm = RandomQueue(size)
        else:
            print 'Error: Choose a different replacement algorithm'
    
    def insert(self, table, data):
        val = self.replacement_algorithm.enqueueLRU(data['key'])
        if val != -1:
            self.hot.delete(table, str(val))
        self.hot.insert(table, data)
        self.hot.commit()
        self.cold.insert(table, data['key'], data)
	

    #TODO error conditions
    def query(self, table, key, cols):
        if not self.replacement_algorithm.contains(key):
            val = self.replacement_algorithm.enqueueLRU(key)
            if val != -1:
                self.hot.delete(table, str(val))
                data = self.cold.table(table).row(key)
                self.hot.insert(table, data)
                self.hot.connection().commit()
        return self.hot.select(table, key, cols)

    def delete(self, table, key):
        if self.replacement_algorithm.delete(key):
            self.hot.delete(table, key)
        self.cold.delete(key)

    def update(self, table, key, data):
        if self.replacement_algorithm.contains(key):
            self.hot.update(table, key, data)
            self.hot.connection().commit()
        self.cold.update(table, key, data)

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
