# 1715. 카드 정렬하기
# https://www.acmicpc.net/problem/1715

import sys
import heapq

sys.stdin = open("5-3_1715.txt", "r")
input = sys.stdin.readline

N = int(input())
heap = []
heapq.heapify(heap)

for i in range(N):
    heapq.heappush(heap, int(input()))

answer = 0

while len(heap) > 1:
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    sum = num1 + num2
    answer += sum
    heapq.heappush(heap, sum)
    
print(answer)