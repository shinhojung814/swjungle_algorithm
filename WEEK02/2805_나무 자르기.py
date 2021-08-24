# 2805. 나무 자르기
# https://www.acmicpc.net/problem/2805

import sys

sys.stdin = open("1-2_2805.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
heights = sorted(list(map(int, input().split())))

left = 0
right = max(heights)

result = 0

while left <= right:
    total = 0
    mid = (left + right) // 2
    
    for height in heights:
        if height > mid:
            total += height - mid
    
    if total < M:
        right = mid - 1
    else:
        result = mid
        left = mid + 1

print(result)