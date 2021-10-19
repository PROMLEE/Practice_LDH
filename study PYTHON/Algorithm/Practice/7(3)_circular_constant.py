def long_add(A, B, C):
    # 세 배열 A, B, C에서, C = A + B
    for i in range(len(A)):
        C[i] = A[i] + B[i]

def long_sub(A, B, C):
    # 세 배열 A, B, C에서, C = A - B
    for i in range(len(A)):
        C[i] = A[i] - B[i]

def long_div(A, b, C):
    # 배열 A를 정수 b로 나누어 배열 C에 저장, C = A/b
    for i in range(len(A)):
        C[i] = A[i]/b

P = int(input("Precision = "))
L = P//4 + 2
K = int(P/1.39894)+1
w, v, q, pi = [0]*L, [0]*L, [0]*L, [0]*L
w[0] = 16*5
v[0] = 4*239
for n in range(1, K+1):
    long_div(w, 5*5, w)
    long_div(v, 239*239, v)
    long_sub(w, v, q)
    long_div(q, 2*n-1, q)
    if n%2 == 1: long_add(pi, q, pi)
    else: long_sub(pi, q, pi)

print(pi) # print pi value in proper format