def solution(name):
    answer = 0
    
    left_right = len(name)
    next_idx = 0
    
    for idx, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        next_idx = idx + 1
        
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
            
        left_right = min(left_right, idx + idx + len(name) - next_idx)
    
    answer += left_right
    
    return answer            
            