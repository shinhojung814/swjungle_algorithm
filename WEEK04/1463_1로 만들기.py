# 1463. 1로 만들기
# https://www.acmicpc.net/problem/1463

import sys

sys.stdin = open("1463_1로 만들기.txt", "r")
input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(N + 1)]

# 2부터 N까지의 수를 탐색
for i in range(2, N + 1):
    # dp[i]는 i를 1로 만들 수 있는 최소 연산 횟수
    dp[i] = dp[i - 1] + 1
    # if만 이용해야 세 연산을 다 거칠 수 있기 때문에 elif나 else를 사용하면 안된다.
    if i % 2 == 0:
        # 1을 더하는 이유는 DP 테이블은 결과가 아닌 계산 횟수를 저장하기 때문이다.
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        # dp[i]에는 1을 더하지 않는 이유는 이미 1을 뺄 때 1을 더해줬기 때문이다.
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])