# 11720. 숫자의 합
# https://www.acmicpc.net/problem/11720

import sys

sys.stdin = open('11720_숫자의 합.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = list(map(str, input().strip()))

result = 0

for i in arr:
    result += int(i)

print(result)