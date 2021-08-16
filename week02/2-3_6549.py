# 6549. 히스토그램에서 가장 큰 직사각형
# https://www.acmicpc.net/problem/6549

import sys

sys.stdin = open("2-3_6549.txt", "r")
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    
    if arr[0] == 0:
        break
    
    heights = arr[1:]
    heights.insert(0, 0)
    heights.append(0)
    
    stack = [0]
    max_square = 0
    
    for i in range(1, arr[0] + 2):
        while stack and heights[i] < heights[stack[-1]]:
            index = stack.pop()
            max_square = max(max_square, (i - stack[-1] - 1) * heights[index])
        stack.append(i)
    print(max_square)