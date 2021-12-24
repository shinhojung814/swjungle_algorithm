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

hidden_num = list(map(str, tmp.split(' ')))
sum_hidden = 0

for j in range(len(hidden_num)):
    if hidden_num[j] != '':
        sum_hidden += int(hidden_num[j])

print(sum_hidden)