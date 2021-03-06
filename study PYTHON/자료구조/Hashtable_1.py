class HashOpenAddr:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None]*self.size
        self.values = [None]*self.size

    def __str__(self):
        s = ""
        for k in self:
            if k == None:
                t = "{0:5s}|".format("")
            else:
                t = "{0:-5d}|".format(k)
            s = s + t
        return s

    def __iter__(self):
        for i in range(self.size):
            yield self.keys[i]

    def find_slot(self, key):
        # key가 존재할 경우 해당 슬롯 번호를, 없으면 삽입될 슬롯 번호를 리턴
        # 테이블이 full이면 None리턴
        i = self.hash_function(key)
        start = i
        while self.keys[i] != None and self.keys[i] != key:
            i = (i+1) % self.size
            if i == start:
                return None
        return i

    def set(self, key, value=None):
        # key가 테이블에 존재한다면 해당 value update
        # key가 테이블에 없다면, key와 value 삽입
        # 테이블이 full이면 None 리턴, 아니면 key값 리턴
        i = self.find_slot(key)
        if i == None:
            return i
        elif self.keys[i] != None:
            self.values[i] = value
            return key
        elif self.keys[i] == None:
            self.keys[i] = key
            self.values[i] = value
            return key
        pass

    def hash_function(self, key):
        return key % self.size

    def remove(self, key):
        # key가 존재할 경우 지우고 key값 리턴, 아니면 None리턴을 리턴
        i = self.find_slot(key)
        if self.keys[i] == None or i == None:
            return None
        else:
            self.keys[i] = None
            j = i
            while True:
                j = (j + 1) % self.size
                if self.keys[j] ==None:
                    break
                k = self.hash_function(self.keys[j])
                if k>i and i>j:
                    continue
                if k>i and j>=k:
                    continue
                if j>=k and i>j:
                    continue
                self.keys[i] = self.keys[j]
                self.keys[j] = None
                i = j
            return key



    def search(self, key):
        # key가 존재할 경우 key리턴(원래는 value리턴해야 함), 아니면 None리턴
        i = self.find_slot(key)
        if i == None or self.keys[i] == None:
            return None
        else:
            return key

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, value):
        self.set(key, value)


# --------------------------------------------------------------------
H = HashOpenAddr()
while True:
    cmd = input().split()
    if cmd[0] == 'set':
        key = H.set(int(cmd[1]))
        if key == None:
            print("* H is full!")
        else:
            print("+ {0} is set into H".format(cmd[1]))
    elif cmd[0] == 'search':
        key = H.search(int(cmd[1]))
        if key == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'remove':
        key = H.remove(int(cmd[1]))
        if key == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            print("- {0} is removed".format(cmd[1]))
    elif cmd[0] == 'print':
        print(H)
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
