# 2606. 바이러스
# https://www.acmicpc.net/problem/2606

import sys

sys.stdin = open("2606_바이러스.txt", "r")
input = sys.stdin.readline

def depth_first(graph, v, visited):
    global cnt
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            depth_first(graph, i, visited)

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (N + 1)
cnt = 0

depth_first(graph, 1, visited)
print(cnt)