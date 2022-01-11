def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    def depth_first(graph, node, visited):
        visited[node] = True;
        
        for index, value in enumerate(graph[node]):
            if index != node:
                if (visited[index] == False) & (value == 1):
                    depth_first(graph, index, visited)
    
    for index, value in enumerate(visited):
        if value == False:
            answer += 1
            
            depth_first(computers, index, visited)
    
    return answer