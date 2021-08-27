# 11053. 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053

import sys

sys.stdin = open("11053_가장 긴 증가하는 부분 수열.txt", "r")
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))