import sys
from collections import deque

sys.stdin = open("2252_줄 세우기.txt", "r")
input = sys.stdin.readline

def topology_sort():
    queue = deque()
    result = []
    
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        current = queue.popleft()
        result.append(current)
        
        for i in graph[current]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    
    print(*result)

N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

topology_sort()