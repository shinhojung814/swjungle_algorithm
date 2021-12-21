# 8595. 히든 넘버
# https://www.acmicpc.net/problem/8595

import sys

sys.stdin = open("8595_히든 넘버.txt", 'r')
input = sys.stdin.readline

N = int(input())
arr = input()

for i in arr:
    if (i) <= 0:
        print(i)