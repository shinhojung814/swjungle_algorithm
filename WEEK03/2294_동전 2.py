# 2294. 동전 2
# https://www.acmicpc.net/problem/2294

import sys
from collections import deque

sys.stdin = open("2294_동전 2.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
arr = set(int(input()) for _ in range(N))
# K원 이하의 값들에 대해 방문 처리
check = [0 for _ in range(K + 1)]

queue = deque()

for num in arr:
    # 동전의 가치가 K원보다 크면 생략
    if num > K:
        continue
    else:
        check[num] = 1
        queue.append([num, 1])

while queue:
    # 동전의 가치를 누적한 합과 사용된 동전의 개수
    sum, cnt = queue.popleft()
    # 누적 합이 K원이라면 flag를 전환하고 사용된 동전의 개수를 출력
    if sum == K:
        print(cnt)
        break
    
    for num in arr:
        if sum + num > K:
            continue
        # 누적 합에 동전을 더한 값에 대해 방문 처리 
        if check[sum + num] == 0:
            check[sum + num] = 1
            # 사용된 동전의 개수를 더하여 누적 합에 동전을 더한 값을 큐에 삽입
            queue.append([sum + num, cnt + 1])

# 주어진 동전으로 K원을 만들 수 없는 경우 -1을 출력
if sum != K:
    print(-1)