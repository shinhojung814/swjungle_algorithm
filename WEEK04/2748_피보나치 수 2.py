# 2748. 피보나치 수 2
# https://www.acmicpc.net/problem/2748

import sys

sys.stdin = open("2748_피보나치 수 2.txt", "r")
input = sys.stdin.readline

N = int(input())

# 메모이제이션을 위해 DP 테이블 초기화
dp = [0] * 100

# 하향식 동적 프로그래밍
def fibonacci(N):
    if N == 1 or N == 1:
        return N
    # 계산 결과가 저장 되있는 경우 저장된 결과 출력
    if dp[N] != 0:
        return dp[N]
    # 계산 결과가 저장되지 않았다면 점화식에 따라서 결과 반환
    dp[N] = fibonacci(N - 2) + fibonacci(N - 1)
    return dp[N]

print(fibonacci(N))