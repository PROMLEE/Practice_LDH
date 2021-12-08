def B(k, col):
    pass


def nQueens(k):
    global solve
    if k > n:
        sol += 1
        return
    for col in range(1, n + 1):
        if B(k, col):
            x[k] = col
            nQueens(k + 1)


n = int(input())
x = [0] * (n + 1)
sol = 0
nQueens(1)
print()
