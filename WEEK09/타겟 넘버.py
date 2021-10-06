# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165

numbers = [1, 1, 1, 1, 1]
target = 3

def solution(numbers, target):
    answer = 0
    
    def depth_first(idx, result):
        nonlocal answer
        
        if idx == len(numbers):
            if result == target:
                answer += 1
            return
        
        else:
            depth_first(idx + 1, result + numbers[idx])
            depth_first(idx + 1, result - numbers[idx])
    
    depth_first(0, 0) 
    return answer

print(solution(numbers, target))