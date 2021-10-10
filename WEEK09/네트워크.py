from collections import deque

def solution(n, computers):
    queue = deque()
    visited = [False for _ in range(n)]
    answer = 0
    
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            queue.append(i)
            
            while len(queue) != 0:
                row = queue.popleft()
                
                for j in range(n):
                    if computers[row][j] == 1 and visited[j] == False:
                        visited[j] = True
                        queue.append(j)
            
            answer += 1
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(solution(n, computers))