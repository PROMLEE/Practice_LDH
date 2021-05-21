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
            print(v.key,end=" ")
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key,end=" ")
            self.inorder(v.right)

    def postorder(self, v):
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key,end=" ")

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
        elif self.search(key)!= None:
            return None
        else:
            n = self.find_loc(key)
            if key > n.key:
                n.right = v
            else:
                n.left = v
        self.size +=1
        return v




T = Tree()

while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        if v != None:
            print("+ {0} is set into H".format(v.key))
        else:
            print(key, "is already in the tree!")
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
