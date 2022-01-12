import sys

sys.stdin = open("DFS_얼려 먹기.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

def solution(graph, node):
    answer = 0
    
    def depth_first(x, y):
        if x < 0 or x >= N or y < 0 or y >= M:
            return False
        
        if graph[x][y] == 0:
            graph[x][y] = 1
            
            depth_first(x - 1, y)
            depth_first(x, y - 1)
            depth_first(x + 1, y)
            depth_first(x, y + 1)
            
            return True
        
        return False
    
    for i in range(N):
        for j in range(M):
            if depth_first(i, j) == True:
                answer += 1
    
    depth_first(node[0], node[1])
    
    return answer

print(solution(graph, (0, 0)))