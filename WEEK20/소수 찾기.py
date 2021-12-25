import sys
from itertools import permutations

def solution(numbers):
    answer = 0
    
    arr = [num for num in numbers]
    permutation = []

    for i in range(1, len(numbers)) + 1:
        permutation += (list(permutations(arr, i)))

    num_list = set(sorted([int("".join(perm)) for perm in permutation]))
    print(num_list)

    for num in num_list:
        check = True
        
        if num < 2:
            continue
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                check = False
                break
        if check:
            answer += 1
    
    return answer
        