# 7569. 도마도
# https://www.acmicpc.net/problem/7569

import sys
from collections import deque

sys.stdin = open("7569_도마도.txt", "r")
input = sys.stdin.readline

def breadth_first():
    M, N, H = map(int, input().rstrip().split())
    arr = [[list(map(int, input().rstrip().split())) for _ in range(N)] for _ in range(H)]

    queue = deque()
    
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 1:
                    queue.append((i, j, k, 0))
    
    dm = [1, 0, 0, -1, 0, 0]
    dn = [0, 1, 0, 0, -1, 0]
    dh = [0, 0, 1, 0, 0, -1]
    
    cnt = 0
    
    while queue:
        z, x, y, cnt = queue.popleft()
        
        for i in range(6):
            nm = y + dm[i]
            nn = x + dn[i]
            nh = z + dh[i]
            
            if 0 <= nm < M and 0 <= nn < N and 0 <= nh < H and arr[nh][nn][nm] == 0:
                arr[nh][nn][nm] = 1
                queue.append((nh, nn, nm, cnt + 1))
    
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 0:
                    return -1
    
    return cnt

print(breadth_first())