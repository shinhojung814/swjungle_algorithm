from collections import deque

def solution(n, vertex):
    vertices = sorted(vertex)
    graph = [[] for i in range(n + 1)]
    route = [0] * (n + 1)

    for vertex in vertices:
        graph[vertex[0]].append(vertex[1])
        graph[vertex[1]].append(vertex[0])

    queue = deque()

    queue.append(1)
    route[1] = 1

    while queue:
        node = queue.popleft()
        
        for j in graph[node]:
            if route[j] == 0:
                queue.append(j)
                route[j] = route[node] + 1
        
    answer = 0
    max_distance = max(route)
    
    for k in route:
        if k == max_distance:
            answer += 1

    return answer