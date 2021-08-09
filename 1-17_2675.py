# 2675. 문자열 반복
# https://www.acmicpc.net/problem/2675

import sys
sys.stdin = open("basic_1-17.txt", "r")

T = int(input())

for num in range(T):
    R, S = map(str, input().split())
    P = ''

    for char in S:
        P += char * int(R)

    print(P)