# 2110. 공유기 설치
# https://www.acmicpc.net/problem/2110

import sys

sys.stdin = open("1-3_2110.txt", "r")
input = sys.stdin.readline

N, C = map(int, input().split())

loc = sorted([int(input()) for i in range(N)])

left = 1
right = loc[-1] - loc[0]
answer = []

while left <= right:
    iptime = 1
    last = loc[0]
    
    mid = (left + right) // 2
    for i in range(1, N):
        if loc[i] - last >= mid:
            iptime += 1
            last = loc[i]
    if iptime < C:
        right = mid - 1
    else:
        left = mid + 1
        answer.append(mid)
        
print(max(answer))