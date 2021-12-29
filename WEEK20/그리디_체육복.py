def solution(n, lost, reserve):
    _lost = set([i for i in lost if i not in reserve])
    _reserve = set([j for j in reserve if j not in lost])
    
    for num in _reserve:
        if num - 1 in _lost:
            _lost.remove(num - 1)
        elif num + 1 in _lost:
            _lost.remove(num + 1)
    
    answer = n - len(_lost)
    
    return answer