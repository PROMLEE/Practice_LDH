def max_sum(A, left, right):
	# A[left], ..., A[right] 중 최대 구간 합 리턴
    if left == right:
        return A[left]

    left_min = float("-inf")
    right_min = float("-inf")
    mid = (left+right)//2

    left_sum = 0
    right_sum = 0
    for i in range(mid, left-1, -1):
        left_sum += A[i]
        left_min = max(left_min, left_sum)
    for i in range(mid+1, right+1):
        right_sum += A[i]
        right_min = max(right_min, right_sum)

    result = max(max_sum(A, left, mid), max_sum(A, mid+1, right))
    result = max(result, left_min+right_min)
    return result

A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A)-1)
print(sol)