# 11399. ATM
# https://www.acmicpc.net/problem/11399

import sys

sys.stdin = open('11399_ATM.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

result = [0] * N

for i in range(N):
    result[i] = sum(arr[:i]) + arr[i]

print(sum(result))