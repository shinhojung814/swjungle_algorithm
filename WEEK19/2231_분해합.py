# 2231. 분해합
# https://www.acmicpc.net/problem/2231

import sys

sys.stdin = open("2231_분해합.txt", 'r')
input = sys.stdin.readline

N = int(input())
res = []

for i in range(N):
    sum = 0
    for j in range(len(str(i))):
        sum += int(str(i)[j])
    if N - sum == i:
        res.append(i)

if res:
    print(min(res))
else:
    print(0)