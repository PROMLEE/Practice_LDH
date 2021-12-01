def histogram(F, B):
    n = len(F)
    DP = [[0 for col in range(B + 1)] for row in range(n)]
    A = []
    for i in range(1, n):
        for j in range(1, B + 1):
            if i < j:
                continue
            if j == 1:
                DP[i][j] = error(F[: i + 1])
            else:
                for k in range(j - 2, i):
                    A.append(DP[k][j - 1] + error(F[k + 1 : i + 1]))
                DP[i][j] = min(A)
                A = []
    return DP[n - 1][B]


def error(A):
    avg = sum(A) / len(A)
    n = 0
    for i in A:
        n += (avg - i) ** 2
    return n


B, n = [int(x) for x in input().split()]
F = []
for i in range(n):
    F.append(int(input()))
a = histogram(F, B)
print(round(a, 3))
# ----------------------------------------------------------------
"""
1. histogram(F, B) 함수 알고리즘 설명
  (1) 리스트A의 오차를 구하는 함수 error(A) 정의
  (2) DP저장용 리스트 DP[i][j] 정의 -> 리스트 F의 i번째 숫자까지를 j개의 그룹으로 나누었을 때 오차의 최소값
  (3) 리스트 F의 len을 n이라 할 때 i(1~n)에 대하여 DP[i][j]를 DP[k][j-1]의 최소값을 사용하여 채운다.
  (4) 이 때, k는 (j-2 ~ i-1)이며 (1)에서 정의한 error(A)를 사용하여 남은 한 그룹의 오차를 구해 더해준다.
  (5) (4)에서 구한 값들을 리스트 A에 append한 후 최솟값을 DP[i][j]에 저장한다.
  (6) 최종적으로, DP[i][j]에는 F의 1~i번째 값들을 j개의 그룹으로 나누었을 때의 최소 오차이다.

2. histogram(F, B) 함수 수행시간 분석
  (1) 1.(1)에서 error(A)의 수행시간은 n
  (2) 1.(3)에서 B * n * error(A)를 n번 반복 수행
    T(n) = B * n * O(n) * n -> O(B*n^3)
"""
