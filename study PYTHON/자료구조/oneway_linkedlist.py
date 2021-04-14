class Node:
	def __init__(self, key=None):
		self.key = key
		self.next = None
	def __str__(self):
		return str(self.key)
	
class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
	
	def __len__(self):
		return self.size
	
	def printList(self): # 변경없이 사용할 것!
		v = self.head
		while(v):
			print(v.key, "->", end=" ")
			v = v.next
		print("None")
	
	def pushFront(self, key):
		a=Node(key)
		a.next=self.head
		self.head=a
		self.size+=1

	def pushBack(self, key):
		a=Node(key)
		if self.size==0:
			self.head=a
		else:
			tail=self.head
			while tail.next != None:
				tail=tail.next
			tail.next= a
		self.size+=1

	def popFront(self): 
		front = link = 0 # head 노드의 값 리턴. empty list이면 None 리턴
		if self.size > 0:
			link= self.head.next
			front=self.head
			self.head=link
			self.size-=1
			return front
		else:
			return None

	def popBack(self):
		tail=self.head# tail 노드의 값 리턴. empty list이면 None 리턴
		if self.size>1:
			while tail.next.next!=None:
				tail=tail.next
			value = tail.next
			tail.next=None
			self.size-=1
			return value
		elif self.size==1:
			value = self.head
			self.head = None
			self.size=0
			return value
		else:
			return None

	def search(self, key):
		v = self.head# key 값을 저장된 노드 리턴. 없으면 None 리턴
		while v:
			if v.key==key:
				return v
			v=v.next
		return None

	def remove(self, x):
		try:
			v=self.search(x.key)# 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
			if self.head==x:
				self.popFront()
			else:
				a = self.head
				while a.next != v:
					a=a.next
				a.next=v.next
				self.size-=1
			return True
		except AttributeError:
			return False

	def size(self):
		return self.size
	
# 아래 코드는 수정하지 마세요!
L = SinglyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == "pushFront":
		L.pushFront(int(cmd[1]))
		print(int(cmd[1]), "is pushed at front.")
	elif cmd[0] == "pushBack":
		L.pushBack(int(cmd[1]))
		print(int(cmd[1]), "is pushed at back.")
	elif cmd[0] == "popFront":
		x = L.popFront()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from front.")
	elif cmd[0] == "popBack":
		x = L.popBack()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from back.")
	elif cmd[0] == "search":
		x = L.search(int(cmd[1]))
		if x == None:
			print(int(cmd[1]), "is not found!")
		else:
			print(int(cmd[1]), "is found!")
	elif cmd[0] == "remove":
		x = L.search(int(cmd[1]))
		if L.remove(x):
			print(x.key, "is removed.")
		else:
			print("Key is not removed for some reason.")
	elif cmd[0] == "printList":
		L.printList()
	elif cmd[0] == "size":
		print("list has", len(L), "nodes.")
	elif cmd[0] == "exit":
		print("DONE!")
		break
	else:
		print("Not allowed operation! Enter a legal one!")