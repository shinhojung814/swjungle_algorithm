from itertools import permutations

def solution(numbers, K):
    arr = list(permutations(numbers, len(numbers)))
    swapped = []

    for permutation in arr:
        differences = []
        
        for i in range(0, len(numbers) - 1):
            differences.append(abs(permutation[i + 1] - permutation[i]))
        
        if max(differences) <= K:
            swapped.append(permutation)
    
    if len(swapped) == 0:
        return -1

    answer = len(numbers)

    for tmp in swapped:
        count = 0
        
        for i in range(len(tmp)):
            if numbers[i] != tmp[i]:
                count += 1
        
        if count - 1 < answer:
            answer = count - 1
    
    return answer

numbers = [10, 40, 30, 20]
K = 20
print(solution(numbers, K))

numbers = [3, 7, 2, 8, 6, 4, 5, 1]
K = 3
print(solution(numbers, K))