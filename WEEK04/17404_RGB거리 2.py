# 17404. RGB거리 2
# https://www.acmicpc.net/problem/17404

import sys

sys.stdin = open("17404_RGB거리 2.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# DP 테이블은 해당 집까지 색칠하는 데에 사용한 총 비용의 최소값을 저장
dp = [[0 for _ in range(3)] for _ in range(N)]

# 최소값을 구하는 문제이기 때문에 result의 초기값을 INF로 설정
result = float('inf')

for i in range(3):
    # 첫번째 집의 색깔을 색칠하는 세 가지 경우의 수
    for j in range(3):
        if j == i:
            dp[0][j] = arr[0][j]
        else:
            # 색칠을 시작하는 색깔이 아닌 경우 색칠하는 비용을 INF로 설정
            dp[0][j] = float('inf')
    
    for k in range(1, N):
        # k번째 집을 색칠하는 비용을 이전까지의 집들을 색칠하는 데에 사용한 총 비용의 최소합에 더한다.
        dp[k][0] = min(dp[k - 1][1], dp[k - 1][2]) + arr[k][0]
        dp[k][1] = min(dp[k - 1][0], dp[k - 1][2]) + arr[k][1]
        dp[k][2] = min(dp[k - 1][0], dp[k - 1][1]) + arr[k][2]
    
    for l in range(3):
        # N번째 집의 색깔이 첫번째 집의 색깔과 다르면 최소값을 result에 저장
        if l != i:
            result = min(result, dp[-1][l])

print(result)