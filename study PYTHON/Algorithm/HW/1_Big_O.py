import time
import random


def evaluate_n2(A, x):
    n = len(A)
    result = 0
    for i in range(0, n):
        u = 1
        for j in range(0, i):
            u *= x
        result += A[i]*u
    return result


def evaluate_n(A, x):
    n = len(A)
    u = 1
    result = 0
    for i in range(0, n):
        result += A[i]*u
        u *= x
    return result


random.seed()  # random 함수 초기화
n = int(input())  # n 입력받음
A = []
for i in range(0, n):
    A.append(random.randint(-1000, 1000))
# 리스트 A를 randint 를 호출하여 n개의 랜덤한 숫자로 채움
x = random.randint(-1000, 1000)

s1 = time.process_time()
print(evaluate_n2(A, x))  # evaluate_n2 호출
e1 = time.process_time()

s2 = time.process_time()
print(evaluate_n(A, x))  # evaluate_n 호출
e2 = time.process_time()

print('evaluate_n2의 수행시간 =', format(e1 - s1, 'E'))
print('evaluate_n의 수행시간 =', '{:.20f}'.format(e2 - s2))
# 두 함수의 수행시간 출력
