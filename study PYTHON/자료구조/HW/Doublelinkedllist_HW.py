class Node:
    def __init__(self, key=None):
        self.key = key
        self.prev = self
        self.next = self

    def __str__(self):
        return str(self.key)


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()  # create an empty list with only dummy node

    def __iter__(self):
        v = self.head.next
        while v != self.head:
            yield v
            v = v.next

    def __str__(self):
        return " -> ".join(str(v.key) for v in self)

    def printList(self):
        v = self.head.next
        print("h -> ", end="")
        while v != self.head:
            print(str(v.key)+" -> ", end="")
            v = v.next
        print("h")

    def splice(self, a, b, x):  # cut [a..b] after x
        if a == None or b == None or x == None:
            return
        # 1. [a..b] 구간을 잘라내기
        a.prev.next = b.next
        b.next.prev = a.prev
        # 2. [a..b]를 x 다음에 삽입하기
        x.next.prev = b
        b.next = x.next
        a.prev = x
        x.next = a

    def moveAfter(self, a, x):  #: 노드 a를 x 뒤로 이동
        # splice(a, a, x)와 같다.
        a.prev.next = a.next
        a.next.prev = a.prev

        x.next.prev = a
        a.next = x.next
        a.prev = x
        x.next = a

    def moveBefore(self, a, x):  # : 노드 a를 노드 x 앞으로 이동
        # splice(a, a, x.prev)와 같다.
        # 1. [a..b] 구간을 잘라내기
        a.prev.next = a.next
        b.next.prev = a.prev
        # 2. [a..b]를 x 다음에 삽입하기
        x.prev = a
        b.next = x.prev.next
        a.prev = x.prev
        x.prev.next = a

    def insertAfter(self, a, key):  # key값을 가지는 새 노드 b를 만들어 a 뒤에 삽입
        if a == None or key == None:
            return None
        b = Node(key)
        b.next = a.next
        b.prev = a
        a.next.prev = b
        a.next = b

    def insertBefore(self, a, key):  # 노드 a 앞에 삽입
        if a == None or key == None:
            return None
        b = Node(key)
        b.prev = a.prev
        b.next = a
        a.prev.next = b
        a.prev = b

    def pushFront(self, key):  # key 값을 가지는 새 노드 b를 만들어 head앞에 삽입 insertAfter() 이용
        if self.head.next == self.head:
            b = Node(key)
            b.next = self.head
            b.prev = self.head
            self.head.next = b
            self.head.prev = b
        else:
            self.insertAfter(self.head, key)

    def pushBack(self, key):  # key 값을 가지는 새 노드 b를 만들어 tail 뒤에 삽입 insertBefore() 이용
        self.insertBefore(self.head, key)

    def deleteNode(self, x):  # delete x
        if x == None or x == self.head:
            return None
        # 노드 x를 리스트에서 분리해내기
        x.prev.next, x.next.prev = x.next, x.prev

    def popFront(self):      # head.next의 값을 리턴, 제거
        if self.head.next == self.head:
            return None
        key = self.head.next.key
        self.deleteNode(self.head.next)
        return key

    def popBack(self):       # head.prev의 값을 리턴, 제거
        if self.head.next == self.head:
            return None
        key = self.head.prev.key
        self.deleteNode(self.head.prev)  # 각자 작성해볼 것!
        return key

    def search(self, key):  # key값이 있으면 해당 노드 리턴, 없으면 None리턴
        v = self.head
        while v.next != self.head:
            v = v.next
            if v.key == key:
                return v
                break

    def isEmpty(self):    # 리스트가 비어 있다면 True 아니면 False 리턴
        if self.head.next == self.head:
            return True
        else:
            return False

    def first(self):      # 리스트의 가장 앞 노드를 리턴, 빈 리스트면 None리턴
        if self.isEmpty():
            return None
        else:
            return self.head.next.key

    def last(self):       # 리스트의 가장 뒷 노드를 리턴, 빈 리스트면 None리턴
        if self.isEmpty():
            return None
        else:
            return self.head.prev.key

    def findMax(self):
        if self.isEmpty():
            return None
        else:
            max_value = self.head.next.key
            v = self.head.next
            while v.next != self.head:
                v = v.next
                if v.key > max_value:
                    max_value = v.key
            return max_value

    def deleteMax(self):
        max_value = self.findMax()
        if max_value != None:  # 최대 key값을 삭제하고 그 최대값을 리턴
            v = self.search(max_value)
            self.deleteNode(v)
        return max_value
        # 만약 빈 리스트라면 None리턴

    def sort(self):
        A = DoublyLinkedList()
        while not self.isEmpty():
            v = self.deleteMax()
            A.pushFront(v)
        self = A
        return self
        # 오름차순으로 정렬 후 정렬된 양방향 리스트 리턴


L = DoublyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == 'pushF':
        L.pushFront(int(cmd[1]))
        print("+ {0} is pushed at Front".format(cmd[1]))
    elif cmd[0] == 'pushB':
        L.pushBack(int(cmd[1]))
        print("+ {0} is pushed at Back".format(cmd[1]))
    elif cmd[0] == 'popF':
        key = L.popFront()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Front".format(key))
    elif cmd[0] == 'popB':
        key = L.popBack()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Back".format(key))
    elif cmd[0] == 'search':
        v = L.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'insertA':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
        x = L.search(int(cmd[1]))
        if x == None:
            print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertAfter(x, int(cmd[2]))
            print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'insertB':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
        x = L.search(int(cmd[1]))
        if x == None:
            print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertBefore(x, int(cmd[2]))
            print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'delete':
        x = L.search(int(cmd[1]))
        if x == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            L.deleteNode(x)
            print("- {0} is deleted".format(cmd[1]))
    elif cmd[0] == "first":
        print("* {0} is the value at the front".format(L.first()))
    elif cmd[0] == "last":
        print("* {0} is the value at the back".format(L.last()))
    elif cmd[0] == "findMax":
        m = L.findMax()
        if m == None:
            print("Empty list!")
        else:
            print("Max key is", m)
    elif cmd[0] == "deleteMax":
        m = L.deleteMax()
        if m == None:
            print("Empty list!")
        else:
            print("Max key", m, "is deleted.")
    elif cmd[0] == 'sort':
        L = L.sort()
        L.printList()
    elif cmd[0] == 'print':
        L.printList()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
