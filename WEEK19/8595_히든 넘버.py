# 8595. 히든 넘버
# https://www.acmicpc.net/problem/8595

import sys

sys.stdin = open("8595_히든 넘버.txt", 'r')
input = sys.stdin.readline

N = int(input())
arr = input()
numbers = '0123456789'
tmp = ''

for i in range(N):
    if arr[i] in numbers:
        tmp += arr[i]
    else:
        tmp += ' '

arr = list(list(map(str, tmp.split(' '))))
answer = 0

for j in range(len(arr)):
    if arr[j] != '':
        answer += int(arr[j])

print(answer)