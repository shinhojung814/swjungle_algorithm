# 2589. 보물섬
# https://www.acmicpc.net/problem/2589

import sys
from collections import deque

sys.stdin = open('2589_보물섬.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def breadth_first(i, j):
    result = 0
    queue = deque()
    queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] != 'W' and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
                    result = max(result, graph[nx][ny])
    
    return result

answer = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] != 'W':
            visited = [[0] * M for _ in range(N)]
            graph[i][j] = 0
            visited[i][j] = 1
            answer = max(answer, breadth_first(i, j))

print(answer)