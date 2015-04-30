from test_select_update_insert import Test
from replacement import System
import time


def main():
    s = System()
    s.setReplacementAlgorithm('LRU', 580)

    print 'begining system test'
    system_start = time.time()
    t1 = Test(s)
    system_read_start = time.time()
    t1.select()
    system_read_end = time.time()
    print 'System read test ended in: ' + str(system_read_end - system_read_start)
    '''system_write_start = time.time()
    t1.insert()
    t1.update()
    system_write_end = time.time()
    print 'System write test ended in: ' + str(system_write_end - system_write_start)
    system_end = time.time()
    print 'System test ended in: ' + str(system_end - system_start)'''



    s2 = System()
    s2.setReplacementAlgorithm('LRU', 0)

    print 'begining hbase test'
    hbase_start = time.time()
    t2 = Test(s2)
    hbase_read_start = time.time()
    t2.select()
    hbase_read_end = time.time()
    print 'Hbase read test ended in: ' + str(hbase_read_end - hbase_read_start)
    '''hbase_write_start = time.time()
    t2.insert()
    t2.update()
    hbase_write_end = time.time()
    print 'Hbase write test ended in: ' + str(hbase_write_end - hbase_write_start)
    hbase_end = time.time()
    print 'Hbase test ended in: ' + str(hbase_end - hbase_start)'''

if __name__ == '__main__':
    main()
