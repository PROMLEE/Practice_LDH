# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math


def matrix_mult(P, C, n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            C[i][j] = math.inf  # math module에서 제공하는 매우 큰 정수
            cost = []
            for k in range(i, j):
                cost.append(C[i][k] + C[k + 1][n] + P[k] * P[k + 1] * P[n + 1])
                C[i][j] = min(cost)
    return C[n][n]


n = int(input())  # n = 행렬 갯수, M_0부터 행렬시작임을 주의!
P = [int(x) for x in input().split()]  # M_i = p_i x p_{i+1}
C = [[0] * n for _ in range(n)]  # 비용을 저장할 2차원 리스트 C 초기화
min_cost = matrix_mult(P, C, n)
print(min_cost)
