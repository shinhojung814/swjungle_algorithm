# DFS - 타겟 넘버

def solution(numbers, target):
    answer = 0
    
    def depth_first(idx, value):
        nonlocal answer
        
        if idx == len(numbers):
            if value == target:
                answer += 1
            return
        else:
            depth_first(idx + 1, value + numbers[idx])
            depth_first(idx + 1, value - numbers[idx])
    
    depth_first(0, 0)
    
    return answer