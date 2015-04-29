import happybase
import json
from DB import DB, DB_NAME, Hbase
from replacementAlgorithms import LRUQueue

'''
Main Client Access Point
'''
class System:

    '''
    Default Constructor
    '''
    def __init__(self):
        self.hot = DB(DB_NAME)
        self.cold = Hbase(DB_NAME)

    '''
    initialize a table
    @param name: name of table
    @param cols: list of tuples of column name and type
    '''
    def initialize(self, name, cols):
        try:
            self.cold.get_connection().create_table(name, {'default':dict()})
        except happybase.hbase.ttypes.AlreadyExists:
            self.cold.get_connection().disable_table(name)
            self.cold.get_connection().delete_table(name)
            self.cold.get_connection().create_table(name, {'default':dict()})
        self.hot.cursor().execute("drop table if exists " + name + ";")
        create_table = "create table " + name + "("
        for key in cols:
            create_table += key + ' ' + cols[key] + ","
        create_table = create_table[:len(create_table) -1] + ");"
        self.hot.cursor().execute(create_table)
        self.hot.connection().commit()

    '''
    load data into table directly into cold storage
    @param table: name of table to be loaded
    @param data_list: list of dictionaries containing dictionaries
    '''
    def load(self, table, data_list):
        for data in data_list:
            if 'key' not in data:
                raise Exception('Error: Must define a key')
            self.cold.insert(table, data['key'], data)

    '''
    Set which replacement algorithm to use
    @param name: name of replacement algorithm
    @param size: maximum size of hot storage
    @exception: Raised if user specifies an incorrect replacement algorithm
    '''
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
            raise Exception('Error: Choose a different replacement algorithm')
    
    '''
    Insert data into both hot and cold storage
    @param table: table to be inserted into
    @param data: dictionary of data to be stored
    @exception: raised if user fails to define key in their data
    '''
    def insert(self, table, data):
        if 'key' not in data:
            raise Exception ('Error: Must define a key')
        val = self.replacement_algorithm.enqueue(data['key'])
        if val != -1:
            self.hot.delete(table, str(val))
        self.hot.insert(table, data)
        self.hot.commit()
        self.cold.insert(table, data['key'], data)
	
    '''
    Query data from table
    @param table: table to be queried from
    @param key: key of data to be queried
    @param cols: list of columns to be returned
    @return: tuple of data 
    '''
    def query(self, table, key, cols):
        if not self.replacement_algorithm.contains(key):
            val = self.replacement_algorithm.enqueue(key) #returns -1 if the queue is full, the key of the data if not
            if val != -1:
                self.hot.delete(table, str(val))
            data = self.stripColumnFamily(self.cold.select(table, key))
            self.hot.insert(table, data)
            self.hot.commit()
        return self.hot.select(table, key, cols)

    '''
    Delete record from table
    @param table: table to be deleted from
    @param key: key of row to be deleted
    '''
    def delete(self, table, key):
        if self.replacement_algorithm.delete(key):
            self.hot.delete(table, key)
            self.hot.commit()
        self.cold.delete(table, key)

    '''
    update record from table
    @param table: table to be updated
    @param key: key of the row to be updated
    @param data: dictonary of column value pairs to be updated
    @exception: thrown if the user attempts to update key
    '''
    def update(self, table, key, data):
        if 'key' in data:
            raise Exception('Cannot update key')
        self.cold.update(table, key, data)
        if self.replacement_algorithm.contains(key):
            self.hot.update(table, key, data)
            self.hot.connection().commit()
        else:
            val = self.replacement_algorithm.enqueue(key)
            if val != -1:
                self.hot.delete(table, str(val))
            data = self.stripColumnFamily(self.cold.select(table, key))
            print data
            self.hot.insert(table, data)
            self.hot.commit()
    '''
    strip column family name from keys
    @param data: dictionary of unstripped column name to values
    @return: dictionary of stripped column names to values
    '''
    def stripColumnFamily(self, data):
        dict = {}
        for key in data:
            dict[key[8:]] = data[key]
        return dict


def main():
    s = System()
    s.setReplacementAlgorithm('LRU', 10)
    s.initialize("test", {'key': 'bigint', 'text': 'varchar(280)'})
    for i in range(20,40):
        s.insert('test', {'key': str(i), 'text': "'helloworld'"})
    print s.query('test', '25', ['key', 'text'])
    s.delete('test', '25')
    s.update('test', '26', {'text': "'whats good'"})

if __name__ == '__main__':
    main()
