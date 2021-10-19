# 방법 1
# def two_sum(X, Y, t):
#     for x in X:
#         for y in Y:
#             if t+x+y > 0:
#                 break
#             if t+x+y == 0:
#                 return True
#     return False

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))

# A.sort()
# B.sort()
# result = False
# for c in C:
#     if two_sum(A, B, c):
#         result = True
#         break
# print(result)

#-----------------------------------------------------

# 방법2
class HashOpenAddr: #Hash table 구현(linear probing)
    def __init__(self, size = 10):
        self.size = size
        self.keys = [None]*self.size
        self.values = [None]*self.size

    def find_slot(self, key):
        i = self.hash_function(key)
        start = i
        while self.keys[i] != None and self.keys[i] != key:
            i = (i+1) % self.size
            if i == start:
                return None
        return i

    def set(self, key, value=None):
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

    def search(self, key):
        i = self.find_slot(key)
        if i == None or self.keys[i] == None:
            return False
        else:
            return True

# two_sum 함수 구현
def two_sum(X, Y, t):
    H = HashOpenAddr(2*len(X)) # Hashtable선언
    # lead factor(LF) = 1/2
    for x in X:
        H.set(x)
        # X의 인수들을 H에 set -> 수행시간 : O(1) X n = O(n)
    for y in Y:
        if H.search((-t)-y):
        # H에서 -t-y에 해당하는 값 search -> 수행시간(unsuccessful search) : O(1) X n = O(n)
            return True
    return False
# two_sum 함수의 수행시간 : a(상수) X O(n) -> O(n)

# A, B, C 리스트 입력받기
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# 판별
result = False
for c in C:
    if two_sum(A, B, c):
        # O(n) X n = O(n^2)
        result = True
        break
#결과 출력
print(result)
