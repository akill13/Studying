#Fist in first out, in python queue from collections import deque
class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self, item):
		return self.items.pop(0)

	def empty(self):
		if not self.items:
			return True
		return False

