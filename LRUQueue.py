'''LRUQueue.py'''
from Queue import PriorityQueue
from Queue import Queue
import time
import calendar
from abc import ABCMeta
'''class for least recently used algorithm'''

class ReplacementQueue(object):

    def enqueue(self, id):
        pass 

    def delete(self, id):
        pass

    def contains(self, id):
        pass

class PriorityQueueContain(PriorityQueue):

    def __delete__(self, id):
	 with self.mutex:
            for tuple in self.queue:
                if(id == tuple[1]):
                    self.queue.remove(tuple) 
                    return True
            return False

class QueueContain(Queue):

    def __contains__(self, id):
        with self.mutex:
            for temp in self.queue:
                if(temp == id):
                    return True
            return False


    def __delete__(self, id):
        with self.mutex:
           for temp in self.queue:
               if(id == temp):
                   self.queue.remove(temp) 
                   return True
           return False


class LRUQueue:
	
    def __init__(self, maxsize):
        self.queue = PriorityQueueContain(maxsize)

    def enqueue(self, id):
        itemLRU = -1
        if(self.queue.full()):
            itemLRU = self.queue.get() 
        self.queue.put((int(time.time()*100000), id))
        return itemLRU

    def contains(self, id):
        isContained = self.delete(id)
        if(isContained):
            self.enqueue(id)
        return isContained
 
    def delete(self, id):
	return self.queue.__delete__(id)


class FIFOQueue(ReplacementQueue):

    def __init__(self, maxsize):
        self.queue = QueueContain(maxsize)

    def enqueue(self, id):
        itemLRU = -1
        if(self.queue.full()):
            itemLRU = self.queue.get() 
        self.queue.put(id)
        return itemLRU

    def contains(self, id):
        return self.queue.__contains__(id)

    def delete(self, id):
        return self.queue.__delete__(id)

'''Used for Testing Purposes'''
def main():
    queue = FIFOQueue(5)
    for i in range(1, 20):
	print i
        queue.enqueue(i)
    queue.contains(15)
    queue.enqueue(20)
    for i in range(1, 21):
        print i, queue.contains(i)
    print queue.delete(20)
    print queue.contains(20)

if __name__ == '__main__':
	main()
