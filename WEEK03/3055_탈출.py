# 3055. 탈출
# https://www.acmicpc.net/problem/3055

import sys
from collections import deque

sys.stdin = open("3055_탈출.txt", "r")
input = sys.stdin.readline

def breadth_first():
    R, C = map(int, input().split())
    queue = deque([])
    maps = []
    visited = [[0 for _ in range(C)] for _ in range(R)]
    start = []
    
    for i in range(R):
        # 좌표 정보를 나타내는 입력값 문자열
        input_str = input().rstrip()
        for j in range(len(input_str)):
            # 비어있는 곳: '.'
            if input_str[j] == '.':
                continue
            # 돌: 'X'
            elif input_str[j] == 'X':
                visited[i][j] = 1
            # 물이 차있는 지역: '*'
            elif input_str[j] == '*':
                # visited값이 2인 경우는 무엇을 의미하는지?
                visited[i][j] = 2
                # 네번째 입력값에 0이면 물큐
                queue.append((i, j, 0, 0))
            # 고슴도치의 위치: 'S'
            elif input_str[j] == 'S':
                start = [i, j]
        maps.append(input_str)
    # 네번째 입력값이 1이면 고슴도치 큐
    queue.append((start[0], start[1], 0, 1))
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    while queue:
        # x, y는 고슴도치가 출발하는 지점의 좌표, cnt는 총 이동 횟수
        x, y, cnt, hedgehog = queue.popleft()
        
        # 이동 가능한 네 개의 방향을 탐색
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            
            # 이동하는 칸이 범위 안에 속하고 돌이 아닌 경우
            if 0 <= tx < R and 0 <= ty < C and maps[tx][ty] != 'X':
                # hedgehog가 0이 아니라면 이 의미하는게 무엇인지?
                if hedgehog:
                    # 새로운 칸을 방문하지 않았을 경우
                    if visited[tx][ty] == 0:
                        # 이동하는 칸이 목표 지점이면
                        if maps[tx][ty] == 'D':
                            # cnt + 1을 출력한다
                            return cnt + 1
                        # visited가 2인 경우가 의미하는 것이 무엇인지?
                        visited[tx][ty] = 2
                        queue.append((tx, ty, cnt + 1, hedgehog))
                else:
                    # visited값이 2이고 비어 있는 칸인 경우
                    if visited[tx][ty] != 2 and maps[tx][ty] == '.':
                        visited[tx][ty] = 2
                        # 새로운 칸을 고슴도치 큐에 삽입
                        queue.append((tx, ty, cnt, hedgehog))
    
    return "KAKTUS"

print(breadth_first())