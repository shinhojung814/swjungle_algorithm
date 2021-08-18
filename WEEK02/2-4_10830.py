# 10830. 행렬 제곱
# https://www.acmicpc.net/problem/10830

import sys

sys.stdin = open("2-4_10830.txt", "r")
input = sys.stdin.readline

N, B = map(int, input().split())
A = []

for i in range(N):
    A.append(list(map(int, input().split())))

def matrix_mul(N, matrix1, matrix2):
    result = [[0 for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 1000
    return result

def matrix_div(N, B, matrix):
    if B == 1:
        return matrix
    elif B == 2:
        return matrix_mul(N, matrix, matrix)
    else:
        temp = matrix_div(N, B // 2, matrix)
        if B % 2 == 0:
            return matrix_mul(N, temp, temp)
        else:
            return matrix_mul(N, matrix_mul(N, temp, temp), matrix)

result = matrix_div(N, B, A)

for i in result:
    for j in i:
        print(j, end=' ')
    print()