class UnorderedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		count = 0
		current = self.head
		while current != None:
			count = count + 1
			current = current.getNext()
		return count

	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else :
				current = current.getNext()
		return found

	def remove(self, item):
		current = self.head
		found = False
		previous = None
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
		# 找到元素后，如果是首元素，直接把head指向第二个元素
		# 否则把previous指向current的next		
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())



		