# K번째수
# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    
    for com in commands:
        answer.append(sorted(array[com[0] - 1 : com[1]])[com[2] - 1])
    
    return answer

arr = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(arr, commands))