def minA(A, i, j):
  if(i == j): return A[i]
  mid = (j-i)//2
  result = min(minA(A, i, mid), minA(A, mid+1, j))
  return result





# def minA(A):
#   n = len(A)
#   S = []
#   a = 0
#   for i in range(n):
#     S.append([0])
#     S[i][0] =A[i]
#     a+=A[i]
#     for j in range(i, n-1):
#       b = min(S[i][j-i], A[j+1])
#       a+=b
#       S[i].append(b)
#   return a

A = [int(x) for x in input().split()]
print(minA(A, 0, len(A)))
# #----------------------------------------------------------------
# '''
# 1. minA(A) 함수 알고리즘 설명
#   (0) 동적계획법을 사용하기 위해 리스트 S 선언, 결과값을 저장하기 위한 변수 a 선언
#   (1) 매 i(0 ~ len(A)-1)에 대하여 S[i][0]에는 A[i]를 저장한다.
#   (2) 매 j(i ~ len(A)-2)에 대하여 S[i][j+1]에는 S[i][j-1]과 A[j+1]중 최솟값을 저장한다.
#   (3) 이때, (1)과 (2)를 실행하기 전 S에 저장할 값들을 a에 더해준다.
#   (4) S[i][j]에는 A[i]~A[i+j]의 최솟값이 저장되게 된다.

# 2. minA(A) 함수 수행시간 분석
#   (1) 1.(3)에서 상수 번의 연산 len(A)-i 번 수행
#   (2) (1.(2)에서 상수 번의 연산 + 2.(1)의 연산 수행)을 n번 수행.
#   (3) 2.(1)과 2.(2)에서 c(상수)번의 연산을 1, 2, ..., n번 수행 -> (n^2+n)/2 번.
#     T(n) = (n^2+n)/2 -> O(n^2)
# '''