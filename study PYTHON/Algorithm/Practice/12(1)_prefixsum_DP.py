n = int(input())
A = [int(x) for x in input().split()]
S = []
S.append(A[0])
for i in range(1, len(A)):
  S.append(max(S[i-1]+A[i], A[i]))
print(max(S))