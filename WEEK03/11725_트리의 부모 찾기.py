# 11725. 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725

import sys

sys.setrecursionlimit(10 ** 8)
sys.stdin = open("11725_트리의 부모 찾기.txt", "r")
input = sys.stdin.readline

def depth_first(graph, v, visited):
    global result
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            result[i].append(v)
            depth_first(graph, i, visited)
            
N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    x, y = input().split()
    graph[int(x)].append(int(y))
    graph[int(y)].append(int(x))

visited = [[] for _ in range(N + 1)]
result = [[] for _ in range(N + 1)]

depth_first(graph, 1, visited)

for ans in result[2:]:
    print(*ans)