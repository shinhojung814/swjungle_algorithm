# 5557. 1학년
# https://www.acmicpc.net/problem/5557

import sys

sys.stdin = open("5557_1학년.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# dp[인덱스][현재까지의 수] = 가능한 경우의 수
dp = [[0] * 21 for _ in range(N)]
# 첫번째 수는 식에 포함되어야 한다.
dp[0][arr[0]] += 1

# i는 두번째부터 N - 2번째 수까지 탐색 
for i in range(1, N - 1):
    # j는 0부터 20까지의 수를 탐색
    for j in range(21):
        # 20까지의 수에서 이전까지의 수를 더한 값이 20보다 작거나 같다면
        if j + arr[i] <= 20:
            dp[i][j + arr[i]] += dp[i - 1][j]
        # 20까지의 수에서 이전까지의 수를 뺀 값이 0보다 크거나 같으면
        if j - arr[i] >= 0:
            dp[i][j - arr[i]] += dp[i - 1][j]

print(dp[N - 2][arr[N - 1]])