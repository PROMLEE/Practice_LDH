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


def get_token_list(expr):
    num = ""
    token = []
    for i in expr:
        if i in '+-*/^()':
            if num != "":
                token.append(num)
                num = ""
            token.append(i)
        elif i == " ":
            continue
        else:
            num = num+i
    if num != "":
        token.append(num)
    return token


def infix_to_postfix(token_list):

    opstack = Stack()
    outstack = []

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
                if opstack.top() == "(":
                    opstack.pop()
                    break
                else:
                    outstack.append(opstack.top())
                    opstack.pop()
        elif token in '+-/*^':
            if len(opstack) == 0:
                opstack.push(token)
            elif prec[token] > prec[opstack.top()]:
                opstack.push(token)
            else:
                while len(opstack) >= 1:
                    if prec[token] <= prec[opstack.top()]:
                        outstack.append(opstack.top())
                        opstack.pop()
                    else:
                        break
                opstack.push(token)
        else:  # operand일 때
            outstack.append(token)

    # opstack 에 남은 모든 연산자를 pop 후 outstack에 append
    while len(opstack) >= 1:
        outstack.append(opstack.top())
        opstack.pop()

    return outstack


def compute_postfix(token_list):
    S = Stack()
    for i in token_list:
        if i in "+-*/^":
            a = float(S.top())
            S.pop()
            b = float(S.top())
            S.pop()
            if i == "+":
                S.push(b+a)
            elif i == "-":
                S.push(b-a)
            elif i == "*":
                S.push(b*a)
            elif i == "/":
                S.push(b/a)
            elif i == "^":
                S.push(b**a)
        else:
            S.push(i)
    return S.top()

    # 아래 세 줄은 수정하지 말 것!
expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)
