# 1931. 회의실 배정
# https://www.acmicpc.net/problem/1931

import sys

sys.stdin = open("1931_회의실 배정.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 회의가 끝나는 시각과 회의가 시작하는 시각 순으로 오름차순 정렬 
arr.sort(key=lambda arr: (arr[1], arr[0]))

cnt = 1
# 첫 회의가 끝나는 시간을 end에 저장
end = arr[0][1]

for i in range(1, N):
    if arr[i][0] >= end:
        cnt += 1
        # 새로운 회의의 끝나는 시각으로 end를 갱신
        end = arr[i][1]

print(cnt)