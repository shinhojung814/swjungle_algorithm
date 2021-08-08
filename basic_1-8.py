# 10950. A+B - 3
# https://www.acmicpc.net/problem/10950

import sys
sys.stdin = open("basic_1-8.txt", "r")

T = int(input())
for num in range(T):
    A, B = map(int, input().split())
    print(A + B)