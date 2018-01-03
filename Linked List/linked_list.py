class Node():
	def __init__(self, value=None):
		self.data = value
		self.next = None

	def __repr__(self):
		return str(self.data)


class LinkedList():
	def __init__(self, value=None):
		self.__root = Node(value)
		self.length = 1 if value else 0


	def __repr__(self):
		output = "["
		tmp = self.__root
		if tmp.data != None:
			while(tmp.next != None):
				output += str(tmp.data) + ", "
				tmp = tmp.next
			output += str(tmp.data)
		return output+"]"


	def __len__(self):
		return self.length


	def __getitem__(self, num):
		if len(self) <= num or num <= -1:
			raise IndexError
		counter = 0
		tmp = self.__root
		if num == 0:
			return tmp
		while(tmp.next != None):
			tmp = tmp.next
			counter += 1
			if counter == num:
				return tmp


	def is_empty(self):
		return self.length == 0


	def add_front(self, item):
		if self.__root.data == None:
			self.__root.data = item
		else:
			new = Node()
			new.data = self.__root.data
			new.next = self.__root.next
			self.__root.data = item
			self.__root.next = new
		self.length += 1


	def add_end(self, item):
		if self.__root.data == None:
			self.__root.data = item
		else:
			tmp = self.__root
			while(tmp.next != None):
				tmp = tmp.next
			new = Node()
			new.data = item
			new.next = None
			tmp.next = new
		self.length += 1


	def remove_front(self):
		if self.length>0:
			tmp = self.__root.next
			self.__root = tmp
			self.length -= 1


	def remove_end(self):
		if self.length > 0:
			tmp = self.__root
			while(tmp.next.next != None):
				tmp = tmp.next
			tmp.next = None
			self.length -= 1



	def clear(self):
		self.__root = Node()
		self.length = 0


	def reverse(self):
		output = LinkedList()
		tmp = self.__root
		while(tmp.next != None):
			output.add_front(tmp.data)
			tmp = tmp.next
		output.add_front(tmp.data)
		return output




if __name__ == "__main__":
	l = LinkedList()
	rev = l.reverse()
	l.add_end(1) #1
	l.add_end(0) #1 0
	l.add_end(7) #1 0 7
	print(l)
	l.add_front(0) #0 1 0 7
	l.add_front(2) #2 0 1 0 7
	l.add_front(9) #9 2 0 1 0 7
	rev = l.reverse()
	print(l)
	print(rev)
	l.remove_end() #9 2 0 1 0
	l.remove_front() #2 0 1 0
	print(l.is_empty())
	print(l)
	l.clear()
	print(l.is_empty())
	print(len(l))




