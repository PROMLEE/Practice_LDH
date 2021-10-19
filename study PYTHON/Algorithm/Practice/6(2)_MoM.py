def find_median_five(L):
    # make L[2] medium
    if len(L) == 5:
        if L[0] > L[2]:
            change_data(L, 0, 2)
        if L[1] > L[2]:
            change_data(L, 1, 2)
        if L[2] > L[3]:
            change_data(L, 2, 3)
        if L[2] > L[4]:
            change_data(L, 2, 4)
        if L[0] > L[1]:
            change_data(L, 0, 1)
        if L[1] > L[2]:
            change_data(L, 1, 2)
        return L[2]
    if len(L) == 4:
        # make L[1] medium
        if L[0] > L[1]:
            change_data(L, 0, 1)
        if L[1] > L[2]:
            change_data(L, 1, 2)
        if L[1] > L[3]:
            change_data(L, 1, 3)
        if L[0] > L[1]:
            change_data(L, 0, 1)
        return L[1]
    if len(L) == 3:
        # make L[1] medium
        if L[0] > L[1]:
            change_data(L, 0, 1)
        if L[1] > L[2]:
            change_data(L, 1, 2)
        if L[0] > L[1]:
            change_data(L, 1, 2)
        return L[1]
    else:
        return L[0]

def change_data(L, a, b):
    temp = L[a]
    L[a] = L[b]
    L[b] = temp

def MoM(A, k):
    a = len(A)
    if a == 1:
        return A[0]
    S, M, L, medians = [], [], [], []
    i = 0
    while i+4 < a:
        medians.append(find_median_five(A[i:i+5]))
        i += 5
    if i < a and i+4 >= a:
        medians.append(find_median_five(A[i:]))
    mom = MoM(medians, len(medians)/2)
    for v in A:
        if v < mom:
            S.append(v)
        elif v > mom:
            L.append(v)
        else:
            M.append(v)
    if len(S) >= k:
        return MoM(S, k)
    elif len(S) + len(M) < k:
        return MoM(L, k-len(M)-len(S))
    else:
        return mom


n, k = list(map(int, input().split()))
L = list(map(int, input().split()))
print(MoM(L, k))