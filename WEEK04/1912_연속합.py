# 1912. 연속합
# https://www.acmicpc.net/problem/1912

import sys

sys.stdin = open("1912_연속합.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(N)]

for i in range(N):
    # dp[i]는 arr[i]까지의 부분수열의 최대합
    dp[i] = max(arr[i], dp[i - 1] + arr[i])

print(max(dp))