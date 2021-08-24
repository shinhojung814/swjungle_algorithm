# 2617. 구슬 찾기
# https://www.acmicpc.net/problem/2617

import sys
from collections import defaultdict

sys.stdin = open("2617_구슬 찾기.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
result = 0

def depth_first(graph, v):
    # 전역변수 global을 이용해 외부에서 선언한 변수 사용
    global cnt
    # v에 대해 방문 처리
    visited[v] = True
    
    # 방문하지 않은 v의 간선을 DFS 함수로 재귀
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            depth_first(graph, i)
    return cnt

# defaultdict()는 딕셔너리 value의 기본값을 설정할 수 있다.
light = defaultdict(list)
heavy = defaultdict(list)

# 주어진 구슬 순서쌍 비교 정보를 리스트에 입력
for x, y in arr:
    light[y].append(x)
    heavy[x].append(y)

# 방문 처리를 기록하는 visited 생성
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    
    # cnt 초기화
    cnt = 0
    
    # 전체 구슬의 절반 이상이 해당 구슬보다 가볍다면 중간 구슬이 될 수 없다. 
    if depth_first(light, i) >= (N + 1) // 2:
        result += 1
    
    # cnt 초기화
    cnt = 0
    
    # 전체 구슬의 절반 이상이 해당 구슬보다 무겁다면 중간 구슬이 될 수 없다.
    if depth_first(heavy, i) >= (N + 1) // 2:
        result += 1

print(result)