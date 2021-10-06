# 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746

numbers1 = [6, 10, 2]
numbers2 = [3, 30, 34, 5, 9]

# from itertools import permutations

# def solution(numbers):
#     arr = [str(num) for num in numbers]
#     arr = list(map(''.join, permutations(arr)))
    
#     answer = 0

#     for i in arr:
#         if int(i) > answer:
#             answer = int(i)
    
#     return str(answer)

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))

# print(solution(numbers1))
# print(solution(numbers2))