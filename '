'''LRUQueue.py'''
from Queue import PriorityQueue
import time

'''class for least recently used algorithm'''
class PriorityQueueContain(PriorityQueue):

	
	def __contains__(self, id):
		with self.mutex:
			for node in self.queue:
				if(id == node.getId()):
					return True
			return False

class LRUQueue:
	
	def __init__(self, maxsize):
		self.queue = PriorityQueueContain(maxsize)
	
	def enqueueLRU(self, id):
		itemLRU = -1
		if(self.queue.full()):
			item = self.queue.get() 
			itemLRU = item.getId()
		newNode = Node(id)
		self.queue.put(newNode)
		return itemLRU

	def contains(self, id):
		return self.queue.__contains__(id)

class Node:
	def __init__(self, id):
		self.id = id
		self.time = time.gmtime()

	def _cmp_(self, other):
		return cmp(self.time, other.time)

	def getId(self):
		return self.id

'''Used for Testing Purposes'''
def main():
	queue = LRUQueue(3)
	for i in range(1, 6):
		queue.enqueueLRU(i)
	for i in range(1, 6):
		print i, queue.contains(i)

if __name__ == '__main__':
	main()
