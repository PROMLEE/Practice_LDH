def max_sum(A):
	# 최대 구간 합 리턴
    P = [A[0]]
    for i in range(1,len(A)):
        P.append(P[i-1]+A[i])
    max = P[0]
    for j in range(1, len(P)):
        if max < P[j]:
            max = a
        for i in range(1, j+2):
            a = P[j] - P[i-1]
            if max < a:
                max = a
    return max

A = [int(x) for x in input().split()]
sol = max_sum(A)
print(sol)