# 1655. 가운데를 말해요
# https://www.acmicpc.net/problem/1655

import sys
import heapq

sys.stdin = open("5-2_1655.txt", "r")
input = sys.stdin.readline

N = int(input())

# left_heap: 최대 힙 / right_heap: 최소 힙
left_heap = []
right_heap = []

# 수빈이가 외친 값 입력
for i in range(N):
    num = int(input())
    # 숫자를 left_heap과 right_heap에 번갈아 가며 입력값을 추가
    if i % 2 == 0:
        # 작은 값들이 저장된 left_heap에서 필요한 값은 최댓값이므로 최대 힙
        heapq.heappush(left_heap, -num)
    else:
        # 큰 값들이 저장된 right_heap에서 필요한 값은 최솟값이므로 최소 힙
        heapq.heappush(right_heap, num)
    
    # 만약 left_heap에서 right_heap보다 큰 값이 저장되었으면 바꿔준다.
    if right_heap and -left_heap[0] > right_heap[0]:
        heapq.heappush(left_heap, -heapq.heappop(right_heap))
        heapq.heappush(right_heap, -heapq.heappop(left_heap))
    
    print(-left_heap[0])