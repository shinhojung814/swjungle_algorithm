def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    

begin, target = "hit", "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))