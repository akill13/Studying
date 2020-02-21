class Stack: #Last in Fist out LIFO
	def __init__(self):
		self.items = []

	def push(self, element):
		self.items.append(element)

	def pop(self):
		return self.items.pop()

	def top(self):
		return self.items[-1]

	def __str__(self):
		return str(self.items)

if __name__ == '__main__':
	#Testing methods
	stack = Stack()
	stack.push(1)
	stack.push(2)
	stack.push(3)
	stack.push(4)

	if stack.items == [1, 2, 3, 4]:
		print('I am working')
	else:
		print(stack)
		print('I am NOT working')

	if 4 == stack.pop():
		print('I am working')
	else:
		print(stack)

	if stack.top == 3:
		print('I am working')
	else:
		print('I am not working')
	
