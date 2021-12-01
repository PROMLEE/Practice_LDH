n = int(input())
S = []
L = [1] * n
count = 0
for i in range(n):
    start, end = map(int, input().split())
    S.append([end, start])
S.sort()
for i in range(n):
    S[i][0], S[i][1] = S[i][1], S[i][0]
for i in range(n):
    if L[i]:
        count += 1
        for j in range(i, n):
            if L[j] == 0:
                continue
            elif S[i][1] >= S[j][0] and S[i][1] <= S[j][1]:
                L[j] = 0
    if 1 not in L:
        break
print(count)
# ----------------------------------------------------------------
"""
1. pinning 알고리즘 설명
    (1) 각 막대의 시작값과 끝값을 이중 리스트 S에 입력받고 끝값을 기준으로 오름차순 정렬한다.
        이때, n개의 인수를 가진 리스트 L을 만들고 1을 채워넣는다.
    (2) 막대의 끝 값이 가장 작은 값 부터 그 끝 값에 못을 꽃고 count에 1을 더한다.
    (3) 이 때 못에 꽂힌 막대는 리스트 L의 해당 위치의 값이 0으로 변한다.
    (4) L의 값이 1인 인수들을 하나씩 지나며 (2), (3)을 반복한다.
    (5) L에 1이 더이상 존재하지 않으면 반복을 종료한다.
    (6) 이 때, count에 저장된 값이 최소 못의 개수이다.

2. pinning 알고리즘 수행시간 분석
    (1) 1.(2)에서 아래의 연산을 n번 반복한다.
    (2) 1.(3)에서 못에 꽂힌 막대를 찾기 위해 상수 번의 연산을 n번 반복한다.
    T(n) = n*n = O(n^2)
"""
