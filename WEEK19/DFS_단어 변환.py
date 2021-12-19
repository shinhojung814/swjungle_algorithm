def solution(begin, target, words):
    answer = 0
    stack = [begin]
    
    if target not in words:
        return 0
    
    while len(words) != 0:
        next = []
        for item in stack:
            for word in words:
                count = 0
                for i in range(len(item)):
                    if word[i] != item[i]:
                        count += 1
                    if count == 2:
                        break
                if count == 1:
                    next.append(word)
                    words.remove(word)
        answer += 1
        
        if target in next:
            return answer
        else:
            stack = next
    
    return answer

begin, target = "hit", "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))