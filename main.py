import time
import concurrent.futures
import sys


class Item:
	def __init__(self, producer, ID):
		self.producer = producer
		self.ID = ID

	def getID(self):
		return self.ID

	def getProducer(self):
		return self.producer


class ItemQueue():
	def __init__(self):
		self.queue = []

	def put(self, item):
		if (len(self.queue) < 50): #I set the length limit of the queue to be 50, you can modify the number if you want to.
			self.queue.append(item)
		else:
			sys.exit()

	def take(self):
		if (len(self.queue) > 0):
			return self.queue.pop()


class Producer:
	def __init__(self, name, sleeptime):
		self.name = name
		self.sleeptime = sleeptime
		self.ID = 0

	def produce(self, ItemQueue):
		while True: #Infinite Loop (However, produce() will not run infinitely since I set the maximum length for the Queue to be 50)
			self.ID += 1
			item = Item(self.name, self.name + str(self.ID))
			ItemQueue.put(item)
			print( f'Producer {item.getProducer()} has created Item ID: {item.getID()}')
			time.sleep(self.sleeptime)


class Consumer:
	def __init__(self, name, sleeptime):
		self.name = name
		self.sleeptime = sleeptime

	def consume(self, ItemQueue):
		while True: #Infinite Loop but will not consume() when the length of the queue is 0.
			s = ItemQueue.take()
			if s is not None:
				print(f'Consumer {self.name} has consumed Item ID: {s.ID}')
			time.sleep(self.sleeptime)
		

#--------------MAIN----------------------------------------------
Q = ItemQueue()
#Notes: The time (in seconds) of sleep can be changed, this affects the rate at which the products are produced and consumed.
A = Producer("A", 0.5)
B = Producer("B", 0.5)
C = Consumer("C", 1.5)
D = Consumer("D", 1.5)
E = Consumer("E", 1.5)

with concurrent.futures.ThreadPoolExecutor() as executor:
	p1 = executor.submit(A.produce, Q)
	p2 = executor.submit(B.produce, Q)

	c1 = executor.submit(C.consume, Q)
	c2 = executor.submit(D.consume, Q) 
	c3 = executor.submit(E.consume, Q)
