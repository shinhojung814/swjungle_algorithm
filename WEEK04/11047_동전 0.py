# 11047. 동전 0
# https://www.acmicpc.net/problem/11047

import sys

sys.stdin = open("11047_동전 0.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
# 가치가 큰 동전을 먼저 사용하기 위해 역순으로 입력
arr = [int(input()) for _ in range(N)][::-1]
# 사용된 동전의 개수
cnt = 0

for num in arr:
    cnt += K // num
    K %= num
    
print(cnt)