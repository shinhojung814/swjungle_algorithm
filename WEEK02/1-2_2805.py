# 2805. 나무 자르기
# https://www.acmicpc.net/problem/2805

import sys

sys.stdin = open("1-2_2805.txt", "r")

N, M = map(int, sys.stdin.readline().split())
height_list = list(map(int, sys.stdin.readline().split()))
height_list.sort()

start = 0
end = max(height_list)

max_height = 0

while start <= end:
    height_sum = 0
    mid = (start + end) // 2
    
    for height in height_list:
        if height > mid:
            height_sum += height - mid
        
    if height_sum < M:
        end = mid - 1
    else:
        max_height = mid
        start = mid + 1

print(max_height)