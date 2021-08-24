# 2110. 공유기 설치
# https://www.acmicpc.net/problem/2110

import sys

sys.stdin = open("1-3_2110.txt", "r")
input = sys.stdin.readline

N, C = map(int, input().split())

loc = sorted([int(input()) for i in range(N)])

left = 1
right = loc[-1] - loc[0]
result = []

while left <= right:
    cnt = 1
    pivot = loc[0]
    
    mid = (left + right) // 2
    for i in range(1, N):
        if loc[i] - pivot >= mid:
            cnt += 1
            pivot = loc[i]
    if cnt < C:
        right = mid - 1
    else:
        left = mid + 1
        result.append(mid)
        
print(max(result))