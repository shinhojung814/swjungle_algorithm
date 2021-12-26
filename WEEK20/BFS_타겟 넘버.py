# BFS - 타겟 넘버

from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([[0, numbers[0]], [0, -1 * numbers[0]]])

    while queue:
        (idx, value) = queue.popleft()
        idx += 1
        
        if idx < len(numbers):
            queue.append([idx, value + numbers[idx]])
            queue.append([idx, value - numbers[idx]])
        else:
            if value == target:
                answer += 1

    return answer