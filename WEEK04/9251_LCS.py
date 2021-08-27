# 9251. LCS
# https://www.acmicpc.net/problem/9251

import sys

sys.stdin = open("9251_LCS.txt", "r")
input = sys.stdin.readline

seq1 = input().rstrip()
seq2 = input().rstrip()

dp = [[0] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]

for i in range(1, len(seq1) + 1):
    for j in range(1, len(seq2) + 1):
        if seq1[i - 1] == seq2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[-1][-1])