import time, random

def prefixSum1(X, n):
    # code for prefixSum1
    S = []
    for i in range(0,n):
        a = 0
        for j in range(0, i+1):
            a += X[j]
        S.append(a)
    return S

def prefixSum2(X, n):
    # code for prefixSum2
    S = [0]*n
    S[0] = X[0]
    for i in range(1, n):
        S[i] = S[i-1] + X[i]
    return S

random.seed()		# random 함수 초기화
n = int(input())     # n 입력받음
X = []
for i in range(0, n):
    a = random.randint(-999, 999)
    X.append(a)
# 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움

before1 = time.process_time()
prefixSum1(X, n)    # prefixSum1 호출
after1 = time.process_time()
before2 = time.process_time()
prefixSum2(X, n)    # prefixSum2 호출
after2 = time.process_time()
print(after1 - before1, after2 - before2)
# 두 함수의 수행시간 출력