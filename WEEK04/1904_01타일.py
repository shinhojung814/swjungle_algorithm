# 1904. 01타일
# https://www.acmicpc.net/problem/1904

import sys

sys.stdin = open("1904_01타일.txt", "r")
input = sys.stdin.readline

N = int(input())

dp = [0] * 1000001

dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746

print(dp[N])