# 1463. 1로 만들기
# https://www.acmicpc.net/problem/1463

import sys

sys.stdin = open("1463_1로 만들기.txt", "r")
input = sys.stdin.readline

X = int(input())

dp = [0 for _ in range(X + 1)]

# 점화식: dp(X) = min(dp(X // 3) + 1, dp(X // 2) + 1, dp(X - 1) + 1)
for i in range(2, X + 1):
    dp[i] = dp[i - 1] + 1
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[X])