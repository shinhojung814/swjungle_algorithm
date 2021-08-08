# 2562. 최댓값
# https://www.acmicpc.net/problem/2562

import sys
sys.stdin = open("basic_1-11.txt", "r")

num_list = []
max_num, max_index = 0, 0
num_index = 1

for num in range(9):
    num = int(input())
    num_list.append(num)

for num in num_list:
    if num > max_num:
        max_num = num
        max_index = num_index
    num_index += 1

print(max_num)
print(max_index)

# data = []

# for _ in range(9):
#     data.append(int(input()))

# print(max(data))
# print(data.index(max(data)) + 1)