# 2178. 미로 탐색
# https://www.acmicpc.net/problem/2178

import sys
from collections import deque

sys.stdin = open("2178_미로 탐색.txt", "r")
input = sys.stdin.readline

def breadth_first(x, y):
    queue = deque()
    queue.append((x, y))
    
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
    
    return graph[N - 1][M - 1]

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(breadth_first(0, 0))