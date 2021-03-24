'''
Infix to postfix
'''


class Stack:
	def __init__(self):
		self.items = []

	def push(self, val):
		self.items.append(val)

	def pop(self):
		try:
			return self.items.pop()
		except IndexError:
			print("Stack is empty")

	def top(self):
		try:
			return self.items[-1]
		except IndexError:
			print("Stack is empty")

	def __len__(self):
		return len(self.items)

	def isEmpty(self):
		return self.__len__() == 0

def infix_to_postfix(infix):
	opstack = Stack()
	outstack = []
	token_list = infix.split(' ')

# 연산자의 우선순위 설정
	prec = {}
	prec['('] = 0
	prec['+'] = 1
	prec['-'] = 1
	prec['*'] = 2
	prec['/'] = 2
	prec['^'] = 3

	for token in token_list:
		if token == '(':
			opstack.push(token)

		elif token == ')':
			while True:
				if opstack.top() =="(":
					opstack.pop()
					break
				else:
					outstack.append(opstack.top())
					opstack.pop()

		elif token in '+-/*^':
			if len(opstack)==0:
				opstack.push(token)
			elif prec[token] > prec[opstack.top()]:
				opstack.push(token)
			else:
				outstack.append(token)
				while prec[token]<=prec[opstack.top()]:
					outstack.append(opstack.top())
					opstack.pop()
		else:
			outstack.append(token)

	while len(opstack)>=1:
		outstack.append(opstack.top())
		opstack.pop()

	return " ".join(outstack)

	
infix_expr = input()
postfix_expr = infix_to_postfix(infix_expr)
print(postfix_expr)