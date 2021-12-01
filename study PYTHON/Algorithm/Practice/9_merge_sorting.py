def merge(A, i, j, k, l):
    # i <= j and j < k <= l
    # 정렬된 두 부분 A[i..j]와 A[k..l]을 merge하는 함수
    B, C = A[i:j+1], A[k:l+1]
    return B, C


def m_sort(A, first, last):
    # 3-way merge sort - merge 함수를 이용해 적절히 합병한다
    if first >= last:
        return A
    middle1 = (first+last)//3
    middle2 = (2*(first+last))//3
    X, Y = merge(A, first, middle1, middle1+1, middle2)
    Z = A[middle2+1:last+1]
    X = m_sort(X, 0, len(X)-1)
    Y = m_sort(Y, 0, len(Y)-1)
    Z = m_sort(Z, 0, len(Z)-1)
    N = X+Y+Z
    B = []
    i = first
    j = middle1+1
    k = middle2+1
    while i <= middle1 and j <= middle2 and k <= last:
        if N[i] <= N[j] and N[i] <= N[k]:
            B.append(N[i])
            i += 1
        elif N[j] <= N[i] and N[j] <= N[k]:
            B.append(N[j])
            j += 1
        else:
            B.append(N[k])
            k += 1
    while i <= middle1 and j <= middle2:
        if N[i] <= N[j]:
            B.append(N[i])
            i += 1
        else:
            B.append(N[j])
            j += 1
    while i <= middle1 and k <= last:
        if N[i] <= N[k]:
            B.append(N[i])
            i += 1
        else:
            B.append(N[k])
            k += 1
    while j <= middle2 and k <= last:
        if N[j] <= N[k]:
            B.append(N[j])
            j += 1
        else:
            B.append(N[k])
            k += 1

    for i in range(i, middle1+1):
        B.append(N[i])
    for j in range(j, middle2+1):
        B.append(N[j])
    for k in range(k, last+1):
        B.append(N[k])
    for l in range(first, last+1):
        A[l] = B[l-first]
    return A


def check(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return A[0]+A[(len(A)//2)]+A[-1]


A = [int(x) for x in input().split()]
m_sort(A, 0, len(A)-1)
print(A)
print(check(A))
