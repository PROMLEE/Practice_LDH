class deque:
    def __init__(self, s):
        self.items = list(s)

    def __len__(self):
        return len(self.items)

    def append(self, c):
        self.items.append(c)

    def appendleft(self, c):
        self.items.insert(0, c)

    def pop(self):
        a = self.items[-1]
        self.items.pop()
        return a

    def popleft(self):
        a = self.items[0]
        self.items.pop(0)
        return a

    def right(self):
        return self.items[-1]

    def left(self):
        return self.items[0]


def check_palindrome(s):
    dq = deque(s)
    palindrome = True
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            palindrome = False
    return palindrome


s = input()
print(check_palindrome(s))
