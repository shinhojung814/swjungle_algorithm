import sys

sys.stdin = open("음료수 얼려 먹기.txt", 'r')
input = sys.stdin.readline

def depth_first(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        depth_first(x - 1, y)
        depth_first(x, y - 1)
        depth_first(x + 1, y)
        depth_first(x, y + 1)
        return True
    return False

N, M = map(int, input().split())
graph = []

for i in range(N):
    graph.append(list(map(int, input().rstrip())))

result = 0

for i in range(N):
    for j in range(M):
        if depth_first(i, j) == True:
            result += 1

print(result)