# 10871. X보다 작은 수
# https://www.acmicpc.net/problem/10871

import sys

sys.stdin = open("1-10_10871.txt", "r")

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
answer = ''

for num in A:
    if num < X:
        answer += str(num)
        answer += ' '

print(answer)