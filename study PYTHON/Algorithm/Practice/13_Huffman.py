from heapq import *

f = [int(x) for x in input().split()]
n = len(f)

T = []

for i in range(n):
    heappush(T, (f[i], str(i)))

while len(T) > 1:
    a = heappop(T)
    b = heappop(T)
    heappush(T, (a[0] + b[0], "(" + a[1] + " " + b[1] + ")"))

s = heappop(T)[1]

nbits = [0] * n
bit = 0
cost = 0
num = ""
for i in s:
    if i == "(":
        if num != "":
            cost += f[int(num)] * bit
            num = ""
        bit += 1
    elif i == ")":
        if num != "":
            cost += f[int(num)] * bit
            num = ""
        bit -= 1
    elif i == " ":
        if num != "":
            cost += f[int(num)] * bit
            num = ""
    else:
        num += i
print(cost)
