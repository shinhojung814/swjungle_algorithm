# 2493. 탑
# https://www.acmicpc.net/problem/2493

import sys

sys.stdin = open("3-5_2493.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
stack = []
answer = [0 for _ in range(len(arr))]

for i in range(len(arr) - 1, -1, -1):
    while stack and arr[stack[-1]] < arr[i]:
       answer[stack.pop()] = i + 1
    stack.append(i)
print(*answer)