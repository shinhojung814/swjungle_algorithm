# 9252. LCS 2
# https://www.acmicpc.net/problem/9252

import sys

sys.stdin = open("9252_LCS 2.txt", "r")
input = sys.stdin.readline

seq1 = input().rstrip()
seq2 = input().rstrip()

dp = [[""] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]

for i in range(1, len(seq1) + 1):
    for j in range(1, len(seq2) + 1):
        if seq1[i - 1] == seq2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + seq1[i - 1]
        else:
            if len(dp[i][j - 1]) > len(dp[i - 1][j]):
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]

result = dp[len(seq1)][len(seq2)]

print(len(result))
if len(result) != 0:
    print(result)