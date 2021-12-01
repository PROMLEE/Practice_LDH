def print_IS(seq, x):
    for i in range(len(seq)):
        if x[i]:
            print(seq[i], end="")
        else:
            print("_", end="")
    print()

def LIS_DP(seq):
  x = ['']*len(seq)
  L = [1]*len(seq)
  n = len(seq)
  x[0] += seq[0]
  for i in range(1, n):
    x[i] += seq[i]
    for j in range(i):
      if seq[j] < seq[i]:
        L[i] = max(L[i], L[j]+1)
        if L[i] == L[j]+1:
          x[i] = seq[i]
          x[i] = x[j]+x[i]
  return max(L), x

seq = input()  # 알파벳 소문자로만 구성된 string 하나가 입력된다
lis, x = LIS_DP(seq)
# print(x)
print(lis)
#------------------------------------------------------------
'''
1. LIS_DP(seq)함수 알고리즘 설명
  (1) DP저장용 리스트 L의 값들을 1로 초기화한다.
  (2) 매 i(1~len(seq))에 대하여 seq의 i번째 알파벳과 seq[j](0~(i-1))를 비교하여
      seq[i]가 더 큰 알파벳이면 L[i]에 L[i]과 (L[j]+1) 중 큰 값을 저장한다.
  (3) 이처럼 (2)연산을 끝내면 L[i]에는 seq[0:i+1]의 가장 긴 부문자열이 저장되게 된다.
  (4) seq의 가장 긴 증가 부문자열을 리턴하려면 max(L)을 리턴하면 된다.

2. LIS_DP(seq)함수 수행시간 분석
  (1) 1.(2)에서 상수 번의 연산 n, n-1, n-2, ... 1번 실행
    T(n) = n(n-1)/2 -> O(n^2)
'''