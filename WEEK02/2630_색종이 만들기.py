# 2630. 색종이 만들기
# https://www.acmicpc.net/problem/2630

import sys

sys.stdin = open("2-1_2630.txt", "r")
input = sys.stdin.readline

N = int(input())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white, blue = 0, 0

def quad_tree(N, x, y):
    global matrix, white, blue
    vertex = matrix[x][y]
    
    for i in range(x, x + N):
        for j in range(y, y + N):
            if vertex != matrix[i][j]:
                quad_tree(N // 2, x, y)
                quad_tree(N // 2, x + N // 2, y)
                quad_tree(N // 2, x, y + N // 2)
                quad_tree(N // 2, x + N // 2, y + N // 2)
                return
    if vertex == 0:
        white += 1
    elif vertex == 1:
        blue += 1

quad_tree(N, 0, 0)

print(white)
print(blue)