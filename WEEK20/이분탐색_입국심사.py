# 이분탐색 - 입국심사

def solution(n, times):
    answer = 0
    
    left, right = 1, max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        total = 0
        
        for time in times:
            total += mid // time
            
        if total >= n:
            answer = mid
            right = mid - 1
        elif total < n:
            left = mid + 1
    
    return answer