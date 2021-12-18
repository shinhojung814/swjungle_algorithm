# 11720. 숫자의 합
# https://www.acmicpc.net/problem/11720

import sys

sys.stdin = open("11720_숫자의 합.txt", 'r')
input = sys.stdin.readline

N = int(input())
num = list(map(str, input().strip()))
sum = 0

for i in num:
    sum += int(i)

print(sum)