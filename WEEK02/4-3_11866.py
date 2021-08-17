# 11866. 요세푸스 문제 0
# https://www.acmicpc.net/problem/11866

import sys
from collections import deque

sys.stdin = open("4-3_11866.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque([i for i in range(1, N + 1)])

answer = []
cnt = 0

while len(queue) >= 1:
    cnt += 1
    if cnt % K == 0:
        queue.rotate(-(K - 1))
        answer.append(queue[0])
        queue.popleft()

print('<', end='')

for j in range(len(answer)):
    if j != len(answer) - 1:
        print("%d, " %answer[j], end='')
    else:
        print("%d>" %answer[j])