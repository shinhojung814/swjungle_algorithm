# 1629. 곱셈
# https://www.acmicpc.net/problem/1629

import sys

sys.stdin = open("2-2_1629.txt", "r")
input = sys.stdin.readline

A, B, C = map(int, input().split())

def divide_conquer(A, B):
    if B == 1:
        return A % C
    
    temp = divide_conquer(A, B // 2)
    
    if B % 2 == 0:
        return temp * temp % C
    
    else:
        return temp * temp * A % C

print(divide_conquer(A, B))