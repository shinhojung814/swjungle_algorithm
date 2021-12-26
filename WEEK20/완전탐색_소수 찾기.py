# 완전 탐색 - 소수 찾기

from itertools import permutations

def solution(numbers):
    answer = 0
    tmp = []
    
    for i in range(1, len(numbers) + 1):
        tmp += list(permutations(numbers, i))
    
    num_list = set(sorted([int("".join(permutation)) for permutation in tmp]))
    
    for num in num_list:
        check = True
        
        if num < 2:
            continue
        
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                check = False

        if check == True:
            answer += 1
    
    return answer