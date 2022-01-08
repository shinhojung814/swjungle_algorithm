import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        try:
            mixed = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        except IndexError:
            return -1
        
        heapq.heappush(scoville, mixed)
        
        answer += 1
        
    return answer