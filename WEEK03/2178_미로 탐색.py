# 2178. 미로 탐색
# https://www.acmicpc.net/problem/2178

import sys
from collections import deque

sys.stdin = open("2178_미로 탐색.txt", "r")
input = sys.stdin.readline

def breadth_first(x, y):
    # 큐를 생성하고 시작점을 큐에 추가
    queue = deque()
    queue.append((x, y))
    
    while queue:
        # 큐에서 (x, y) 좌표를 확인
        x, y = queue.popleft()
        
        # (x, y)의 상하좌우를 탐색
        for i in range(4):
            # 기존 x값에 -1, 0, 1을 더한다
            nx = x + dx[i]
            # 기존 y값에 -1, 0, 1을 더한다
            ny = y + dy[i]
            
            # 새로운 좌표가 범위를 벗어나면 넘어간다
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 새로운 좌표가 이동 불가능하면 넘어간다
            if graph[nx][ny] == 0:
                continue
            # 새로운 좌표가 이동 가능하면 새로운 좌표로 이동
            if graph[nx][ny] == 1:
                # 새로운 좌표로 이동하며 이동 횟수를 1 추가
                graph[nx][ny] = graph[x][y] + 1
                # 새로운 좌표를 큐에 추가
                queue.append([nx, ny])
    
    # 목표 지점에 도착하기 까지의 이동 횟수를 출력
    return graph[N - 1][M - 1]

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

print(breadth_first(0, 0))