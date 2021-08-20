# 1987. 알파벳
# https://www.acmicpc.net/problem/1987

import sys

sys.setrecursionlimit(10 ** 8)
sys.stdin = open("1987_알파벳.txt", "r")
input = sys.stdin.readline

def breadth_first():
    R, C = map(int, input().rstrip().split())
    alphabet = [list(input()) for _ in range(R)]
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    answer = 0
    
    queue = set()
    queue.add((0, 0, 1, alphabet[0][0]))
    
    while queue:
        x, y, cnt, visited = queue.pop()
        answer = max(answer, cnt)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < R and 0 <= ny < C:
                if alphabet[nx][ny] not in visited:
                    queue.add((nx, ny, cnt + 1, visited + alphabet[nx][ny]))
                    
    return answer

print(breadth_first())