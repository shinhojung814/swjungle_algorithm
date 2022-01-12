from collections import deque

def breadth_first(graph, start, visited):
    queue = deque([start])
    
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [False] * len(graph)

breadth_first(graph, 1, visited)