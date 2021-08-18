# 2812. 크게 만들기
# https://www.acmicpc.net/problem/2812

import sys

sys.stdin = open("3-8_2812.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
num = list(input().rstrip())

stack = []
iter = K

for i in range(N):
    while iter > 0 and stack and stack[-1] < num[i]:
        stack.pop()
        iter -= 1
    stack.append(num[i])

print(''.join(stack[:N - K]))