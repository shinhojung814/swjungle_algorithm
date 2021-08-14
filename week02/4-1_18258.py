# 18258. 큐 2
# https://www.acmicpc.net/problem/18258

import sys
from collections import deque

sys.stdin = open("4-1_18258.txt", "r")
input = sys.stdin.readline

queue = deque()

N = int(input())

arr = [input().split('\n')[0] for i in range(N)]

for str in arr:
    if str.split()[0] == 'push':
        queue.append(str.split()[1])
    elif str == 'pop':
        if len(queue) != False:
            print(queue[0])
            queue.popleft()
        else:
            print(-1)
    elif str == 'size':
        print(len(queue))
    elif str == 'empty':
        if len(queue) != False:
            print(0)
        else:
            print(1)
    elif str == 'front':
        if len(queue) != False:
            print(queue[0])
        else:
            print(-1)
    elif str == 'back':
        if len(queue) != False:
            print(queue[-1])
        else:
            print(-1)