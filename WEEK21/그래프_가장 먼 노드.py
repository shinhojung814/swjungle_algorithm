from collections import deque

def solution(n, edge):
    vertices = sorted(edge)
    graph = [[] for _ in range(n + 1)]
    route = [0] * (n + 1)
    
    for vertex in vertices:
        graph[vertex[0]].append(vertex[1])
        graph[vertex[1]].append(vertex[0])
    
    queue = deque()
    queue.append(1)
    route[1] = 1
    
    while queue:
        node = queue.popleft()
        
        for i in graph[node]:
            if route[i] == 0:
                queue.append(i)
                route[i] = route[node] + 1
    
    answer = 0
    max_distance = max(route)
    
    for j in route:
        if j == max_distance:
            answer += 1
    
    return answer