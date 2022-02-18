def knapsack(i, size):
    global K, n, P, S, MP, x
    if i >= n or size <= 0:
        return
    p = 0
    s = 0
    p += sum(P[j] for j in range(0, i) if x[j] == 1)
    s += sum(S[j] for j in range(0, i) if x[j] == 1)
    # x[i] = 1을 따라가야 하는 지 결정
    if s + S[i] <= K:  # 물건 i가 크기 제한을 넘지 않아야
        B = frac_knapsack(n - i, S[i:], P[i:], size - S[i])
        if p + P[i] + B > MP:
            MP = max(MP, p + P[i])
            x[i] = 1
            knapsack(i + 1, size - S[i])
    # x[i] = 0을 따라가야하는지 결정
    B = frac_knapsack(n - i, S[i:], P[i:], size)
    if p + B > MP:
        x[i] = 0
        knapsack(i + 1, size)


def frac_knapsack(n, S, P, K):
    global x
    if K <= 0:
        return 0
    p = 0
    s = 0
    p += sum(P[j] for j in range(0, n) if x[j] == 1)
    s += sum(S[j] for j in range(0, n) if x[j] == 1)
    for i in range(n):
        if s + S[i] <= K:
            p += P[i]
            s += S[i]
        else:
            p += (K - s) * (P[i] / S[i])
            s = K
            break
    return p


K = int(input())
n = int(input())
S = list((int(x) for x in input().split()))
P = list((int(x) for x in input().split()))
A = []
for i in range(n):
    z, a, b = S[i] / P[i], P[i], S[i]
    A.append([z, a, b])
A.sort()
P = [0] * n
S = [0] * n
for i in range(n):
    P[i], S[i] = A[i][1], A[i][2]
MP = 0
x = [0] * n
knapsack(0, K)
print(MP)
