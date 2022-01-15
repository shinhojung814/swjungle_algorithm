import sys
from collections import deque

sys.stdin = open("1260_DFS와 BFS.txt", "r")
input = sys.stdin.readline

def depth_first(graph, node, visited):
    visited[node] = True
    graph[node].sort()
    print(node, end=' ')
    
    for i in graph[node]:
        if not visited[i]:
            depth_first(graph, i, visited)

def breadth_first(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        graph[node].sort()
        print(node, end=' ')
        
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited1 = [False for _ in range(N + 1)]
visited2 = [False for _ in range(N + 1)]

depth_first(graph, V, visited1)
print()
breadth_first(graph, V, visited2)