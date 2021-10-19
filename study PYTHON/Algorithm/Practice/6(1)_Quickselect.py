def QuickSelect(L, k):
    A, M, B = [], [], []
    pivot = L[0]
    for i in L:
        if i < pivot:
            A.append(i)
        elif i == pivot:
            M.append(i)
        else:
            B.append(i)
    if len(A) >= k:
        return QuickSelect(A, k)
    elif len(A)+len(M) < k:
        return QuickSelect(B, k-len(A)-len(M))
    else:
        return pivot

n, k = list(map(int, input().split()))
L = list(map(int,input().split()))
print(QuickSelect(L, k))
