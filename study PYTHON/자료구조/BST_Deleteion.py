class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

    def __str__(self):
        return str(self.key)


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def preorder(self, v):
        if v != None:
            print(v.key, end=" ")
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key, end=" ")
            self.inorder(v.right)

    def postorder(self, v):
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=" ")

    def find_loc(self, key):
        if self.size == 0:
            return None
        par = self.root.parent
        v = self.root
        while True:
            if v == None:
                return par
            elif v.key == key:
                return v
            elif v.key < key:
                par = v
                v = v.right
            else:
                par = v
                v = v.left

    def search(self, key):
        v = self.find_loc(key)
        if v.key == key:
            return v
        else:
            return None

    def insert(self, key):
        v = Node(key)
        if self.size == 0:
            self.root = v
        elif self.search(key) != None:
            return None
        else:
            n = self.find_loc(key)
            if key > n.key:
                n.right = v
            else:
                n.left = v
            v.parent = n
        self.size += 1
        return v

    def deleteByMerging(self, x):
        a = x.left
        b = x.right
        pt = x.parent
        if a == None:
            c = b
        else:
            c = m = a
            while m.right:
                m = m.right
            m.right = b
            if b:
                b.parent = m
        if self.root == x:
            if c:
                c.parent = None
            self.root = c
        else:
            if pt.left == x:
                pt.left = c
            else:
                pt.right = c
            if c:
                c.parent = pt
        self.size -= 1

    def deleteByCopying(self, x):
        L = x.left
        R = x.right
        pt = x.parent
        if L:
            y = L
            while y.right:
                y = y.right
            x.key = y.key
            if y.left:
                m = y.left
                if x.left == y:
                    x.left == y.left
                else:
                    y.parent.right = y.left
                m.parent = y.parent
            else:
                if x.left == y:
                    x.left = y.left
                else:
                    y.parent.right = None
        elif R:
            y = R
            while y.left:
                y = y.left
            x.key = y.key
            if y.right:
                m = y.right
                if x.right == y:
                    x.right = y.right
                else:
                    y.parent.left = y.right
                m.parent = y.parent
            else:
                if x.right == y:
                    x.right = x.left
                else:
                    y.parent.left = None
        elif pt:
            if pt.right == x:
                pt.right = None
            else:
                pt.left = None
        else:
            self.root = None
        self.size -= 1


T = Tree()

while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'deleteC':
        v = T.search(int(cmd[1]))
        T.deleteByCopying(v)
        print("- {0} is deleted by copying".format(int(cmd[1])))
    elif cmd[0] == 'deleteM':
        v = T.search(int(cmd[1]))
        T.deleteByMerging(v)
        print("- {0} is deleted by merging".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
