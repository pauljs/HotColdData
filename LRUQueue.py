'''LRUQueue.py'''
from Queue import PriorityQueue
import time
import calendar

'''class for least recently used algorithm'''
class PriorityQueueContain(PriorityQueue):

	
    def __contains__(self, id):
        with self.mutex:
            for node in self.queue:
                if(id == node.getId()):
                    node.updateTime()
                    return True
            return False

    def __remove__(self, id):
	 with self.mutex:
            for node in self.queue:
                if(id == node.getId()):
                    self.queue.remove(node) 
                    return True
            return False

            itemLRU = -1

            if(len(self.queue) == self.maxsize):
                print "blah"
                item = self.get() 
                itemLRU = item.getId()
            newNode = Node(id)
            self.put(newNode)
            print id
            return itemLRU



class LRUQueue:
	
    def __init__(self, maxsize):
        self.queue = PriorityQueueContain(maxsize)
	
    def enqueueLRU(self, id):
        itemLRU = -1

        if(self.queue.full()):
            itemLRU = self.queue.get()[1] 
        self.queue.put((int(time.time()*100000), id))

        return itemLRU

    def contains(self, id):
	for tuple in self.queue.queue:
           if(tuple[1] == id):
               return True
        return False
 
    def remove(self, id):
	    return self.queue.__remove__(id)


def main():
    queue = LRUQueue(10)
    for i in range(1, 100):
        queue.enqueueLRU(i)
    for i in range(1, 100):
        print i, queue.contains(i)
   # queue.remove(5)

if __name__ == '__main__':
	main()
