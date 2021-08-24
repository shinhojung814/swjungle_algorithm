# 2164. 카드2
# https://www.acmicpc.net/problem/2164

import sys
from collections import deque

sys.stdin = open("4-2_2164.txt", "r")
input = sys.stdin.readline

N = int(input())

queue = deque()

for i in range(1, N + 1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue[0])
    queue.popleft()

print(int(queue[0]))