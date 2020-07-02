class Queue:

	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		self.items.pop()

	def print_queue(self):
		print(self.items)

	def is_empty(self):
		return self.items == []

	def size(self):
		return len(self.items)


def queueTest():
	queue = Queue()
	queue.enqueue(1)
	queue.enqueue(2)
	print(queue.print_queue())
	queue.dequeue()

if __name__=="__main__":
	queueTest()