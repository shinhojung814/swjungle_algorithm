# 1946. 신입 사원
# https://www.acmicpc.net/problem/1946

import sys

sys.stdin = open("1946_신입 사원.txt", "r")
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda arr: arr[0])
    
    cnt = 1
    # 1차 최고 성적 지원자의 2차 성적을 max로 설정
    max = arr[0][1]

    for i in range(1, N):
        if max > arr[i][1]:
            # i번 지원자의 2차 성적이 max보다 좋다면 cnt에 1 추가
            cnt += 1
            # i번 지원자의 2차 성적을 max로 설정
            max = arr[i][1]

    print(cnt)