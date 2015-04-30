'''LRUQueue.py'''
from Queue import PriorityQueue
from Queue import Queue
import time
import calendar
from abc import ABCMeta
import random
'''class for least recently used algorithm'''

class ReplacementQueue(object):

    '''
    Checks whether the ReplacementQueue is full.
    Returns True if it is full and false otherwise.
    '''
    def isFull(self):
        pass

    '''
    Adds object to this ReplacementQueue. If ReplacementQueue
    is full then new object will replace an old object
    based on the replacement algorithm. If the ReplacementQueue
    is not full, then will add the new object, without removing another,
    depending on the ReplacementQueue algorithm for enqueue'''
    def enqueue(self, id):
        pass 

    '''
    Deletes an object if it is in the ReplacementQueue.
    Returns True if object was deleted in the ReplacementQueue, else False.
    '''
    def delete(self, id):
        pass

    '''
    Checks to see if object is in the ReplacementQueue.
    Returns True if so, else False.
    '''
    def contains(self, id):
        pass

    '''
    Prints the contents of the ReplacementQueue
    as well as other informational data pertaining to each
    replacement algorithm
    '''
    def printContents(self):
        pass

class PriorityQueueContain(PriorityQueue):

    def __delete__(self, id):
	 with self.mutex:
            for tuple in self.queue:
                if(id == tuple[1]):
                    self.queue.remove(tuple) 
                    return True
            return False
    def __printContents__(self):
        print 'Length: ' + str(len(self.queue))
        for id in self.queue:
            print id

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

    def __printContents__(self):
        print 'Length: ' + str(len(self.queue))
        for id in self.queue:
            print id

class LRUQueue:
	
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.queue = PriorityQueueContain(maxsize)

    def clear(self):
        self.queue = PriorityQueueContain(self.maxsize)

    def isFull(self):
        return self.queue.full()

    def enqueue(self, id):
        item = (-1, -1)
        if(self.isFull()):
            item = self.queue.get() 
        self.queue.put((int(time.time()*100000), id))
        return item[1]

    def contains(self, id):
        isContained = self.delete(id)
        if(isContained):
            self.enqueue(id)
        return isContained
 
    def delete(self, id):
	return self.queue.__delete__(id)

    def printContents(self):
        self.queue.__printContents__()

class FIFOQueue(ReplacementQueue):

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.queue = QueueContain(maxsize)

    def clear(self):
        self.queue = QueueContain(self.maxsize)

    def isFull(self):
        return self.queue.full()

    def enqueue(self, id):
        item = -1
        if(self.isFull()):
            item = self.queue.get() 
        self.queue.put(id)
        return item

    def contains(self, id):
        return self.queue.__contains__(id)

    def delete(self, id):
        return self.queue.__delete__(id)

    def printContents(self):
        self.queue.__printContents__()

class ClockStaticQueue(ReplacementQueue):

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.queueTracker = Queue(maxsize)
        for i in range (0, maxsize):
            self.queueTracker.put(i)
        self.clock = [None] * maxsize
        self.hand = 0

    def clear(self):
        maxsize = self.maxsize
        self.queueTracker = Queue(maxsize)
        for i in range (0, maxsize):
            self.queueTracker.put(i)
        self.clock = [None] * maxsize
        self.hand = 0


    def isFull(self):
        return not self.queueTracker.empty()

    def incrementHand(self):
        self.hand = (self.hand + 1) % self.maxsize

    def enqueue(self, id):
        item = (-1, -1)
        if(self.contains(id)):
            return item
        elif(self.isFull()):
            nextEmptyIndex = self.queueTracker.get()
            self.clock[nextEmptyIndex] = (1, id)
        else:
            '''clock is full'''
            while(True):
                if(self.clock[self.hand] is None):
                    self.incrementHand()
                    continue
                if(self.clock[self.hand][0] == 0):
                    break
                self.clock[self.hand] = (0, self.clock[self.hand][1])
                self.incrementHand()
            item = self.clock[self.hand][1]
            self.clock[self.hand] = (1, id)
            self.incrementHand()
        return item[1]

    def delete(self, id):
        for i in range(0, self.maxsize):
            if(self.clock[i] and self.clock[i][1] == id):
                self.clock[i] = None
                self.queueTracker.put(i)
                if(self.hand == i):
                    self.incrementHand()
                return True
        return False

    def contains(self, id):
        for tuple in self.clock:
            if(tuple is None):
                continue
            if(tuple[1] == id):
                tuple = (1, id)
                return True
        return False

    def printContents(self):
        print "Hand: " + str(self.hand)
        for tuple in self.clock:
             print tuple

class ClockDynamicQueue(ReplacementQueue):

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.clock = []
        self.hand = 0

    def clear(self):
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
        item = (-1, -1)
        if(self.contains(id)):
            return item
        elif(not self.isFull()):
            self.clock.append((1, id))
        else:
            '''clock is full'''
            while(self.clock[self.hand][0] == 1):
                self.clock[self.hand] = (0, self.clock[self.hand][1])
                self.incrementHand()
            item = self.clock[self.hand][1]
            self.clock[self.hand] = (1, id)
            self.incrementHand()
        return item[1]

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
            if(tuple is None):
                continue
            if(tuple[1] == id):
                return True
        return False

    def printContents(self):
        print "Hand:" + str(self.hand)
        for tuple in self.clock:
            print tuple

class RandomQueue(ReplacementQueue):

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.clock = []

    def clear(self):
        self.clock = []

    def isFull(self):
        return len(self.clock) == self.maxsize

    def enqueue(self, id):
        item = -1
        if(self.contains(id)):
            return item
        elif(not self.isFull()):
            self.clock.append(id)
        else:
            '''clock is full'''
            removalIndex = random.randint(0, self.maxsize - 1)
            item = self.clock[removalIndex]
            del self.clock[removalIndex]
            self.clock.append(id)
        return item

    def delete(self, id):
        for i in range(0, self.maxsize):
            if(self.clock[i] == id):
                del self.clock[i]
                return True
        return False

    def contains(self, id):
        for temp in self.clock:
            if(temp == id):
                return True
        return False

    def printContents(self):
        print "Length: " + str(len(self.clock))
        for i in range(0, len(self.clock)):
            print self.clock[i]

'''Used for Testing Purposes'''
def main():
    queue = FIFOQueue(4)
    print "\n"
    print queue.printContents() 
    queue.enqueue(1)
    print "\n"
    print queue.printContents() 
    queue.enqueue(2)
    print "\n"
    print queue.printContents() 
    queue.enqueue(3) 
    print "\n"
    print queue.printContents() 
    queue.enqueue(4) 
    print "\n"
    print queue.printContents() 
    queue.enqueue(5)  
    print "\n"
    print queue.printContents() 
    print queue.delete(1)
    print queue.delete(3)
    print queue.printContents()
    queue.enqueue(6)
    print "\n", queue.printContents()

if __name__ == '__main__':
	main()
