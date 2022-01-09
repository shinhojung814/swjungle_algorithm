def solution(n, times):
    answer = 0
    
    left, right = 1, n * max(times)
    
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