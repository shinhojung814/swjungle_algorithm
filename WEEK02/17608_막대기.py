# 17608. 막대기
# https://www.acmicpc.net/problem/17608

import sys

sys.stdin = open("3-4_17608.txt", "r")
input = sys.stdin.readline

N = int(input())
stack = [int(input()) for i in range(N)]

longest = 0
cnt = 0

for stick in stack[::-1]:
    if stick > longest:
        longest = stick
        cnt +=1

print(cnt)