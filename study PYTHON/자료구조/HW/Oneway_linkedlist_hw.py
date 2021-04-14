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

    def printList(self):  # 변경없이 사용할 것!
        v = self.head
        while(v):
            print(v.key, "->", end=" ")
            v = v.next
        print("None")

    def pushFront(self, key):
        a = Node(key)
        a.next = self.head
        self.head = a
        self.size += 1

    def pushBack(self, key):
        a = Node(key)
        if self.size == 0:
            self.head = a
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = a
        self.size += 1

    def popFront(self):
        # head 노드의 값 리턴. empty list이면 None 리턴
        front = link = 0  # head 노드의 값 리턴. empty list이면 None 리턴
        if self.size > 0:
            link = self.head.next
            front = self.head
            self.head = link
            self.size -= 1
            return front
        else:
            return None

    def popBack(self):
        tail = self.head  # tail 노드의 값 리턴. empty list이면 None 리턴
        if self.size > 1:
            while tail.next.next != None:
                tail = tail.next
            value = tail.next
            tail.next = None
            self.size -= 1
            return value
        elif self.size == 1:
            value = self.head
            self.head = None
            self.size = 0
            return value
        else:
            return None

    def search(self, key):
        v = self.head  # key 값을 저장된 노드 리턴. 없으면 None 리턴
        while v:
            if v.key == key:
                return v
            v = v.next
        return None

    def remove(self, x):
        try:
            v = self.search(x.key)  # 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
            if self.head == x:
                self.popFront()
            else:
                a = self.head
                while a.next != v:
                    a = a.next
                a.next = v.next
                self.size -= 1
            return True
        except AttributeError:  # x.key를 정의하지 못할 경우
            return False

    def reverse(self, key):
        if self.size <= 1:
            pass
        elif self.search(key) != None:
            if self.head.key == key:
                v = self.popBack()
                self.pushFront(v.key)
                v = self.head
            else:
                v = self.head
                while v.next.key != key:
                    v = v.next
            while True:
                x = self.popBack()
                self.size += 1
                x.next = v.next
                v.next = x
                v = v.next
                if v.next == None or v.next.next == None:
                    break
        # key값을 갖는 노드 x가 없다면 아무일도 하지 않는다.

    def findMax(self):
        if self.size == 0:  # self가 empty이면 None
            return None
        else:  # max key 리턴
            max_key = self.head.key
            v = self.head
            while v.next != None:
                v = v.next
                if v.key > max_key:
                    max_key = v.key
            return max_key

    def deleteMax(self):
        # 최대 key값을 찾아 해당 노드를 제거 후, key리턴
        # self가 empty이면 None, 아니면 max key 지운 후, max key 리턴
        # 힌트 : findmax, search, remove 조합)
        if self.size == 0:
            return None
        else:
            max_key = self.findMax()
            v = self.search(max_key)
            self.remove(v)
            return max_key

    def insert(self, k, key):
        # head노드부터 k번째 노드 다음에 key를 갖는 새로운 노드 삽입
        # (k>0)이라 가정.
        # 노드 개수가 k보다 작다면 가장 뒤에 삽입(pushBack)
        a = Node(key)
        if self.size >= k:
            v = self.head
            for i in range(k-1):
                v = v.next
            a.next = v.next
            v.next = a
            self.size += 1
        else:
            self.pushBack(key)

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
    elif cmd[0] == "reverse":
        L.reverse(int(cmd[1]))
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
    elif cmd[0] == "insert":
        L.insert(int(cmd[1]), int(cmd[2]))
        print(cmd[2], "is inserted at", cmd[1]+"-th position.")
    elif cmd[0] == "printList":
        L.printList()
    elif cmd[0] == "size":
        print("list has", len(L), "nodes.")
    elif cmd[0] == "exit":
        print("DONE!")
        break
    else:
        print("Not allowed operation! Enter a legal one!")
