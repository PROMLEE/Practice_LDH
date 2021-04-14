import random
import time


def unique_n(A):
    try:
        B = list(range(0, n*2+1))
        # 음수를 포함한 A가 가질수 있는 모든 정수의 갯수(2n+1개)와 같은 갯수를 가진 리스트 B생성
        for i in A:  # A의 인수 차례대로 불러오기
            if B[i] == "":
                # 리스트 B의 i위치에 있는 인수에서 공백 식별
                raise notimplementederror
                # 리스트 B의 i위치에서 공백이 식별되면 err발생
            else:
                B[i] = ""  # 해당 값이 존재했다는 것을 표시
            # 리스트의 B의 i위치에서 공백이 식별되지 않을 시 해당 자리 인수를 공백으로 변환
        print("Yes")
    except:
        print("No")


def unique_nlogn(A):
    try:
        A.sort()
        for i in range(0, n-1):
            if A[i] == A[i+1]:  # 정렬된 모든 i와 그보다 한단계 더 크거나 같은 수 비교
                raise notimplementederror  # 서로 같은 수 발견시 err발생
        print("Yes")
    except:
        print("No")


def unique_n2(A):
    try:
        for i in range(0, n):
            for j in range(0, n):
                if i != j and A[i] == A[j]:  # 모든 i와 j에 대하여 비교
                    raise notimplementederror  # 서로 같은 수 발견시 err발생
        print("Yes")
    except:
        print("No")


# input: 값의 개수 n
n = int(input())
# -n과 n 사이의 서로 다른 값 n 개를 랜덤 선택해 A 구성
A = random.sample(range(-n, n+1), n)

# 위의 세 개의 함수를 차례대로 불러 결과 값 출력해본다
before1 = time.process_time()
unique_n(A)
after1 = time.process_time()

before2 = time.process_time()
unique_nlogn(A)
after2 = time.process_time()

before3 = time.process_time()
unique_n2(A)
after3 = time.process_time()
# 당연히 모두 다르게 sample했으므로 YES가 세 번 연속 출력되어야 한다
# 동시에 각 함수의 실행 시간을 측정해본다
print(after1-before1, after2-before2, after3-before3)
# 이러한 과정을 n을 100부터 10만까지 다양하게 변화시키면서 측정한다
