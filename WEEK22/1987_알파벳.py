import sys
from collections import deque

sys.stdin = open("1987_알파벳.txt", "r")
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]

def depth_first(x, y):
    queue = deque()
    queue.append([x, y])
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    while queue:
        x, y = queue.popleft()
        count = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            
            if graph[nx][ny] == graph[x][y]:
                continue
            
            if graph[nx][ny] != graph[x][y]:
                count += 1
                queue.append([nx, ny])
    
    return count

