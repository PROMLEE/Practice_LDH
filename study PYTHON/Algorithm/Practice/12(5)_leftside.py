W = int(input())
words = input().split()
length = []
for i in range(len(words)):
    length.append(len(words[i]))
DP = [0] * (len(words) + 1)
DP[1] = (W - len(words[0])) ** 3
for i in range(2, len(words) + 1):
    A = []
    for j in range(0, i):
        x = sum(length[j:i])
        y = i - j - 1
        if x + y <= W:
            A.append(DP[j] + (W - x - y) ** 3)
        DP[i] = min(A)
print(DP)
# -------------------------------------------------------------------
"""
  1.
"""
