import sys

def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == student1[i % 5]:
            scores[0] += 1
        if answers[i] == student2[i % 8]:
            scores[1] += 1
        if answers[i] == student3[i % 10]:
            scores[2] += 1
    
    answer = []
    
    for idx, num in enumerate(scores):
        if scores[idx] == max(scores):
            answer.append(idx + 1)
    
    return answer