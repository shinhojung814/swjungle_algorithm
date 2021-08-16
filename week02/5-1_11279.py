# 11279. 최대 힙
# https://www.acmicpc.net/problem/11279

import sys
import heapq

sys.stdin = open("5-1_11279.txt", "r")
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    cmd = int(input())
    if not cmd:
        # 힙이 비어있지 않으면 최솟값 출력
        if heap:
            print(-(heapq.heappop(heap)))
        # 비어있으면 0 출력
        else:
            print(0)
    else:
        heapq.heappush(heap, -cmd)

heap = []

for _ in range(N):
    cmp = int(input())
    if not cmd:
        if heap:
            print(-(heapq.heappop(heap)))
        else:
            print(0)
    else:
        heapq.heappush(heap, -cmd)