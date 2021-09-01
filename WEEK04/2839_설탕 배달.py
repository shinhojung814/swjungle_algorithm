# 2839. 설탕 배달
# https://www.acmicpc.net/problem/2839

import sys

sys.stdin = open("2839_설탕 배달.txt", "r")
input = sys.stdin.readline

N = int(input())

result = 0

while True:
    # 5로 나눈 몫을 결과값에 더한다.
    if N % 5 == 0:
        result += (N // 5)
        print(result)
        break
    
    # 5로 나누어지지 않으면 3을 빼고 결과값을 1 더한다.
    N -= 3
    result += 1
    
    # 3보다 작고 0이 아니면 -1을 출력
    if 0 < N < 3:
        print(-1)
        break