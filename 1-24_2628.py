# 2628. 종이자르기
# https://www.acmicpc.net/problem/2628

import sys
sys.stdin = open("basic_1-24.txt", "r")

width, height = map(int, input().split())
width_list, height_list = [width], [height]

for num in range(int(input())):
    num1, num2 = map(int, input().split())
    if num1 == 0:
        height_list.append(num2)
    else:
        width_list.append(num2)

width_list.append(0)
height_list.append(0)

width_list.sort(reverse=True)
height_list.sort(reverse=True)

width_diff_list = []
height_diff_list = []

for width in range(0, len(width_list) - 1):
    width_diff_list.append(width_list[width] - width_list[width + 1])
    
for height in range(0, len(height_list) - 1):
    height_diff_list.append(height_list[height] - height_list[height + 1])

print(max(width_diff_list) * max(height_diff_list))