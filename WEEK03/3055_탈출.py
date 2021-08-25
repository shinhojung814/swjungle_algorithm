# 3055. 탈출
# https://www.acmicpc.net/problem/3055

import sys
from collections import deque

sys.stdin = open("3055_탈출.txt", "r")
input = sys.stdin.readline

def breadth_first():
    R, C = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(R)]
    queue = deque()
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    # 물이 차있는 지역과 고슴도치를 큐에 삽입
    for i in range(R):
        for j in range(C):
            # 해당 지역이 목표 지점인 경우
            if arr[i][j] == 'D':
                D = [i, j]
            # 해당 지역이 물이 차있는 지역인 경우
            elif arr[i][j] == '*':
                queue.append([i, j, '*'])
            # 해당 지역이 고슴도치의 위치인 경우
            elif arr[i][j] == 'S':
                S = [i, j, 0]
    queue.append(S)
    
    while queue:
        # z는 고슴도치를 큐에 삽입한다는 것과 이동 시간을 의미
        x, y, z = queue.popleft()
        # 목표 지점에 도착하면 z를 출력
        if x == D[0] and y == D[1]:
            print(z)
            break
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 이동하는 지역이 범위를 벗어나는 경우
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    continue
                else:
                    # 이동하는 지역이 목표 지점, 물이 이미 차있는 지역과 바위가 아닌 경우
                    if z == '*' and arr[nx][ny] != 'D' and arr[nx][ny] != '*' and arr[nx][ny] != 'X':
                        arr[nx][ny] = '*'
                        queue.append([nx, ny, '*'])
                    # 이동하는 지역이 비어있는 곳이거나 목표 지점인 경우
                    elif type(z) == int and (arr[nx][ny] == '.' or arr[nx][ny] == 'D'):
                        arr[nx][ny] = z + 1
                        queue.append([nx, ny, z + 1])
        # 큐가 빌 때까지 목표 지점에 도착하지 못하는 경우
        if len(queue) == 0:
            print("KAKTUS")

breadth_first()