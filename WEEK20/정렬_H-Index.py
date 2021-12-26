# 정렬 - H-Index

def solution(citations):
    answer = 0
    
    for i in range(len(citations)):
        count = 0
        
        for j in range(len(citations)):
            if citations[j] >= i + 1:
                count += 1
        
        if count >= i + 1:
            answer += 1

    return answer