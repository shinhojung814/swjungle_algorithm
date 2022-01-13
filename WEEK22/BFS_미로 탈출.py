import sys
from collections import deque

sys.stdin = open("BFS_미로 탈출.txt", "r")
input = sys.stdin.readline

def solution(graph, node):
    def breadth_first(x, y):
        queue = deque()
        queue.append((x, y))
        
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                
                if graph[nx][ny] == 0:
                    continue
                
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
        
        answer = graph[N - 1][M - 1]
        
        return answer
    
    return breadth_first(0, 0)

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

print(solution(graph, (0, 0)))