# 정렬 - 가장 큰 수

from itertools import permutations

def solution(numbers):
    arr = list(permutations(numbers, len(numbers)))
    num_list = []
    
    for perm in range(len(arr)):
        tmp = ''
        for num in range(len(numbers)):
            tmp += str(arr[perm][num])
        num_list.append(int(tmp))
    
    answer = str(max(num_list))
    
    return answer