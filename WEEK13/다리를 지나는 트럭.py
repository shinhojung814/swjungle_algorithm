# 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583

import sys
from collections import deque

sys.stdin = open('다리를 지나는 트럭.txt', 'r')
input = sys.stdin.readline

def solution(bridge_length, weight, truck_weights):
    answer = 0
    # trucks_queue는 다리를 지나가는 트럭의 무게의 큐
    trucks_queue = [0] * bridge_length
    
    # 다리를 지나는 트럭이 있으면 반복 시행
    while trucks_queue:
        # 트럭 한 대가 지나갈 때마다 1초 추가
        answer += 1
        trucks_queue.pop(0)
        
        # 지나가야 할 트럭이 남아 있으면
        if truck_weights:
            # 지나가는 트럭들과 다음 트럭의 무게의 합이 버틸 수 있는 무게를 넘지 않으면
            if sum(trucks_queue) + truck_weights[0] <= weight:
                # 남아 있는 트럭에서 꺼내어 지나가는 트럭 큐에 추가 
                trucks_queue.append(truck_weights.pop(0))
            
            # 버틸 수 있는 무게를 넘으면 지나갈 때 까지 기다린다.
            else:
                trucks_queue.append(0)
    
    return answer