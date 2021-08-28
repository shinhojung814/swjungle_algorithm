# 2748. 피보나치 수 2
# https://www.acmicpc.net/problem/2748

import sys

sys.stdin = open("2748_피보나치 수 2.txt", "r")
input = sys.stdin.readline

N = int(input())

# 메모이제이션을 위해 DP 테이블 초기화
dp = [0] * 100

# 하향식 동적 프로그래밍
def fibonacci(num):
    if num == 0 or num == 1:
        return num
    # 계산 결과가 저장 되있는 경우 저장된 결과 출력
    if dp[num] != 0:
        return dp[num]
    # 계산 결과가 저장되지 않았다면 점화식에 따라서 결과 반환
    dp[num] = fibonacci(num - 2) + fibonacci(num - 1)
    return dp[num]

print(fibonacci(N))