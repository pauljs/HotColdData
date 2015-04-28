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
        item = -1
        if(self.queue.full()):
            item = self.queue.get() 
        self.queue.put((int(time.time()*100000), id))
        return item

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
        item = -1
        if(self.queue.full()):
            item = self.queue.get() 
        self.queue.put(id)
        return item

    def contains(self, id):
        return self.queue.__contains__(id)

    def delete(self, id):
        return self.queue.__delete__(id)

class ClockIndexQueue(ReplacementQueue):

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.queueTracker = Queue(maxsize)
        for i in range (0, maxsize):
            self.queueTracker.put(i)
        self.clock = [None] * maxsize
        self.hand = 0

    def incrementHand(self):
        self.hand = (self.hand + 1) % self.maxsize

    def enqueue(self, id):
        item = -1
        if(not self.queueTracker.empty()):
            nextEmptyIndex = self.queueTracker.get()
            self.clock[nextEmptyIndex] = (1, id)
        elif(self.contains(id)):
            pass
        else:
            '''clock is full'''
            while(True):
                if(self.clock[self.hand] == None):
                    self.incrementHand()
                    continue
                if(self.clock[self.hand][0] == 0):
                    break
                self.clock[self.hand] = (0, self.clock[self.hand][1])
                self.incrementHand()
            item = self.clock[self.hand][1]
            self.clock[self.hand] = (1, id)
            self.incrementHand()
        return item

    def delete(self, id):
        for i in range(0, self.maxsize):
            if(self.clock[i] and self.clock[i][1] == id):
                self.clock[i] = None
                self.queueTracker.put(i)
                if(self.hand == i):
                    self.incrementHand()
                return True
        return False

    def printContents(self):
        print "Hand: " + str(self.hand)
        for tuple in self.clock:
             print tuple

class ClockRemoveQueue(ReplacementQueue):

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.clock = []
        self.hand = 0

    def incrementHand(self):
        if(len(self.clock) == 0 or self.hand == len(self.clock)):
            '''second or is edge case for when delete last element in list'''
            self.hand = 0
        self.hand = (self.hand + 1) % len(self.clock)

    def isFull(self):
        return len(self.clock) == self.maxsize

    def enqueue(self, id):
        item = -1
        if(not self.isFull()):
            self.clock.append((1, id))
        elif(self.contains(id)):
            pass
        else:
            '''clock is full'''
            while(self.clock[self.hand][0] == 1):
                self.clock[self.hand] = (0, self.clock[self.hand][1])
                self.incrementHand()
            item = self.clock[self.hand][1]
            self.clock[self.hand] = (1, id)
            self.incrementHand()
        return item

    def delete(self, id):
        for i in range(0, self.maxsize):
            if(self.clock[i][1] == id):
                del self.clock[i]
                if(self.hand == len(self.clock)):
                    self.incrementHand()
                return True
        return False

    def contains(self, id):
        for tuple in self.clock:
            if(tuple[1] == id):
                tuple = (1, id)
                return True
        return False

    def printContents(self):
        print "Hand:" + str(self.hand)
        for tuple in self.clock:
            print tuple

def main():
    queue = ClockIndexQueue(4)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3) 
    queue.enqueue(4) 
    queue.enqueue(1) 
    queue.enqueue(2)
    queue.printContents()
    print "\n"
    queue.enqueue(5) 
    queue.printContents()
    queue.enqueue(1) 
    queue.enqueue(2) 
    queue.enqueue(3) 
    queue.enqueue(4) 
    queue.enqueue(5) 
    queue.printContents()

    queue.delete(2)
    queue.printContents()
    queue.delete(3)
    queue.printContents()
    '''for i in range(1, 20):
	print i
        queue.enqueue(i)
    queue.contains(15)
    queue.enqueue(20)
    for i in range(1, 21):
        print i, queue.contains(i)
    print queue.delete(20)
    print queue.contains(20)
    '''

if __name__ == '__main__':
	main()
