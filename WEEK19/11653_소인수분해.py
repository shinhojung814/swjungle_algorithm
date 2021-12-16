# 11653. 소인수분해
# https://www.acmicpc.net/problem/11653

import sys

sys.stdin = open("11653_소인수분해.txt", 'r')
input = sys.stdin.readline

N = int(input())

while N > 1:
    for i in range(2, N + 1):
        if N % i == 0:
            print(i)
            N //= i
            break