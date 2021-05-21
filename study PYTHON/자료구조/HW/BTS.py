class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
        self.height = 0 # 높이 정보도 유지함에 유의!!

    def __str__(self):
        return str(self.key)

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def preorder(self, v):
        if v != None:
            print(v.key, end=' ')
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key, end=' ')
            self.inorder(v.right)

    def postorder(self, v):
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=' ')

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
        if v:
            if v.key == key:
                return v
            else:
                return None
        return None

    def find_height(self, t):
    # t노드부터 가장 낮은 노드까지의 거리 + 1
        if t == None:
            return 0
        else:
            left = self.find_height(t.left)
            right = self.find_height(t.right)
            if left > right:
                return left+1
            else:
                return right+1
    def reload_height(self, x):
        while x:
            x.height = self.find_height(x)-1
            x = x.parent

    def insert(self, key):
        # 노드들의 height 정보 update 필요
        v = Node(key)
        if self.size == 0:
            self.root = v
        else:
            p = self.find_loc(key)
            if p.key == key:
                return v
            if p and p.key != key:
                if p.key < key: p.right = v
                else: p.left = v
                v.parent = p
        self.reload_height(v)
        self.size += 1
        return v

    def deleteByMerging(self, x):
        a = x.left
        b = x.right
        pt = x.parent
        if a == None:
        # x의 왼쪽 자식노드가 없으면 c = b
            c = b
        else:
        # 왼쪽 자식노드가 있으면 c = a
            c = m = a
            while m.right: # a에서 가장 큰 노드 m 찾기
                m = m.right
            m.right = b # m의 오른쪽 자식노드에 b 추가
            if b:
                b.parent = m
            self.reload_height(b)
        if self.root == x: # x 가 루트노드이면
            if c:
                c.parent = None
            self.root = c
        else: # x 가 루트노드가 아니면 c를 x자리에
            if pt.left == x:
                pt.left = c
            else:
                pt.right = c
            if c:
                c.parent = pt
            self.reload_height(pt)
        self.size -= 1

    def deleteByCopying(self, x):
        L = x.left
        R = x.right
        pt = x.parent
        if L:
            y = L
            while y.right: # L중 가장 큰 노드 y찾기
                y = y.right
            x.key = y.key # y의 key를 x의 key로 카피
            if y.left: # y의 왼쪽 노드를 y자리로 올리기
                m = y.left
                if x.left == y: # y의 parent가 x일때
                    x.left = y.left # x의 왼쪽 노드로 올리기
                else: # 나머지는 원래 y 자리로
                    y.parent.right = y.left
                m.parent = y.parent
            else:
                if x.left == y:
                    x.left = y.left
                else:
                    y.parent.right = y.left
            self.reload_height(y)
        elif R:
            y = R
            while y.left:
                y = y.left
            x.key = y.key
            if y.right:
                m = y.right
                if x.right == y:
                    x.right = m
                else:
                    y.parent.left = m
                m.parent = y.parent
            else:
                if x.right == y:
                    x.right = y.right
                else:
                    y.parent.left = y.right
            self.reload_height(y)
        elif pt:
            if pt.right == x:
                pt.right = None
            else:
                pt.left = None
            self.reload_height(pt)
        else:
            self.root = None
        self.size -= 1

    def height(self, x): # 노드 x의 height 값을 리턴
        if x == None: return -1
        else: return x.height

    def succ(self, x): # key 값의 오름차순 순서에서 x.key 값의 다음노드(successor) 리턴
        # x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴
        a = None
        pt = None
        if x == None: return a
        if x.right:
            a = x.right
            while a.left:
                a = a.left
        if x.parent:
            n = x
            pt = x.parent
            while pt.parent:
                if pt.left == n:
                    break
                n = pt
                pt = pt.parent
            if pt.key < x.key:
                pt = None
        if a and pt:
            if a.key < pt.key: return a
            else: return pt
        elif a: return a
        elif pt: return pt
        else: return a

    def pred(self, x): # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
        # x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴
        a = None
        pt = None
        if x == None: return a
        if x.left:
            a = x.left
            while a.right:
                a = a.right
        if x.parent:
            n = x
            pt = x.parent
            while pt.parent:
                if pt.right == n:
                    break
                n = pt
                pt = pt.parent
            if pt.key > x.key:
                pt = None
        if a and pt:
            if a.key > pt.key: return a
            else: return pt
        elif a: return a
        elif pt: return pt
        else: return a

    def rotateLeft(self, x): #균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        a = x.right
        if a == None: return
        b = a.left
        a.parent = x.parent
        if x.parent:
            if x.parent.left == x:
                x.parent.left = a
            else:
                x.parent.right = a
        a.left = x
        x.parent = a
        x.right = b
        if b: b.parent = x
        if x == self.root and x:
            self.root = a
        self.reload_height(x)

    def rotateRight(self, x): #균형이진탐색트리의 1차시 동영상 시청 필요(height 정보 수정 필요)
        a = x.left
        if a == None: return
        b = a.right
        a.parent = x.parent
        if x.parent:
            if x.parent.left == x:
                x.parent.left = a
            else:
                x.parent.right = a
        a.right = x
        x.parent = a
        x.left = b
        if b: b.parent = x
        if x == self.root and x:
            self.root = a
        self.reload_height(x)



T = BST()

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
    elif cmd[0] == 'height':
        h = T.height(T.search(int(cmd[1])))
        if h == -1:
            print("= {0} is not found!".format(cmd[1]))
        else:
            print("= {0} has height of {1}".format(cmd[1], h))
    elif cmd[0] == 'succ':
        v = T.succ(T.search(int(cmd[1])))
        if v == None:
            print("> {0} is not found or has no successor".format(cmd[1]))
        else:
            print("> {0}'s successor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'pred':
        v = T.pred(T.search(int(cmd[1])))
        if v == None:
            print("< {0} is not found or has no predecssor".format(cmd[1]))
        else:
            print("< {0}'s predecssor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'Rleft':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateLeft(v)
            print("@ Rotated left at node {0}".format(cmd[1]))
    elif cmd[0] == 'Rright':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateRight(v)
            print("@ Rotated right at node {0}".format(cmd[1]))
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
