def solve(L, S):
  D = [[0], [0]]
  for i in range(1, S+1):
    if i<10:
      D[1].append(1)
    else:
      D[1].append(0)
  for i in range(2, L+1):
    D.append([0])
    for j in range(1, S+1):
      if(j<10):
        D[i].append(sum(D[i-1][1:j+1]))
      else:
        D[i].append(sum(D[i-1][j-9:j+1]))
  return D[L][S]

L, S = [int(x) for x in input().split()]
print(solve(L, S)%2147483647)
#----------------------------------------
'''
1. solve(L, S) 함수 알고리즘 설명
  (1) 자리수(i)가 1이면 1~9까지의 경우 값만 존재하므로 D[1][1~9] -> 1, 나머지는 0 저장
  (2) 자리수(i)가 2 이상이면 D[i][1~9] -> sum(D[i-1][1~j]), 나머지는 sum(D[i-1][j-9~j]) 저장
  (3) 이처럼 D[L]까지 반복하면 D[L][S]에는 L자리의 모든 합이 S가 되는 자연수의 개수가 저장되게 된다.

2. solve(L, S) 함수 수행시간 분석
  (1) 1.(2)에서 상수 번의 연산을 L*S번 수행
    T(n) = O(L*S) -> O(n^2)
'''