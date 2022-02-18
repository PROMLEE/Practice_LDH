def print_subset(x):
    print([A[i] for i in range(len(x)) if x[i]])


def subset_sum(k):
    global p
    v_sum = 0
    v_sum += sum(A[j] for j in range(k) if x[j])
    if k == len(A):
        if v_sum == S:
            p = True
            print_subset(x)
    else:
        if v_sum + A[k] == S:
            x[k] = 1
            p = True
            print_subset(x)
        elif v_sum + A[k] <= S:
            x[k] = 1
            subset_sum(k + 1)
        x[k] = 0
        subset_sum(k + 1)


p = False
A = list(set(int(x) for x in input().split()))
A.sort()
S = int(input())
x = [0] * len(A)
subset_sum(0)
if not p:
    print([])
