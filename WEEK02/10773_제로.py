# 10773. 제로
# https://www.acmicpc.net/problem/10773

import sys

sys.stdin = open("3-2_10773.txt", "r")
input = sys.stdin.readline

K = int(input())

num_list = [int(input()) for i in range(K)]
stack = []

for num in num_list:
    if num != 0:
        stack.append(num)
    else:
        stack.pop(-1)

print(sum(stack))