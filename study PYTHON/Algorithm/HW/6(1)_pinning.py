def pin(S, F):
    a = min(S)
    b = max(F)
    L = []
    for i in range(a, b + 1):
        L.append(pinned(S, F, i))
    return max(L)


def pinned(S, F, n):
    x = len(S)
    M = []
    N = []
    count = 0
    for i in range(x):
        if S[i] <= n:
            M.append(i)
    for i in M:
        if F[i] >= n:
            N.append(i)
    count = len(N)
    return count


n = int(input())
S = [0] * n
F = [0] * n
for i in range(n):
    S[i], F[i] = map(int, input().split())
print(pin(S, F))
# ----------------------------------------------------------------
"""
1. pin 함수 알고리즘 설명
    (1) pin 함수에서 입력받은 막대의 시작 값의 최솟값과 끝 값의 최댓값을 구해 저장한다.
    (2) (1)에서 구한 최솟값부터 최댓값을 차례로 pinned 함수에 넣어 해당 위치에 꽂히는 막대의 갯수를 구한다.
    (3) pinned 함수에서는 시작값 S와 끝 값 F와 위치 s를 입력받아 못을 위치 s에 꽂았을 때 꽂히는 막대의 개수이다.
    (4) pinned 함수는 먼저 빈 리스트 M에 시작값이 s보다 작은 막대의 인덱스를 저장한다.
    (5) M에 저장되어있는 막대 중 끝 값이 s보다 큰 막대의 인덱스를 리스트 N에 저장한다.
    (6) 이때 N에 있는 막대의 갯수가 꽂힌 막대의 갯수이고 이 갯수들을 모은 것을 함수 pin에서 L에 저장하고 L의 최댓값을 구한다.

2. pin 함수 알고리즘 수행시간 분석
    (1) 모든 막대들의 총 길이를 B라 할때, 함수 pin에서 pinned함수를 B번 반복 실행한다.
    (2) pinned 함수에서는 상수 번의 연산을 n번 실행한다.
    T(n) = B*n = O(B*n) -> 이떄, B는 입력받는 막대의 범위의 좌표 최댓값-최솟값
"""
