# 10871. X보다 작은 수
# https://www.acmicpc.net/problem/10871

import sys
sys.stdin = open("basic_1-10.txt", "r")

N, X = map(int, input().split())
A = list(map(int, input().split()))
answer = ''

for num in A:
    if num < X:
        answer += str(num)
        answer += ' '

print(answer)

# 다른 풀이
# N, X = map(int, input().split())
# A = list(map(int, input().split()))

# ans_list = []

# for i in A:
#     if i < X:
#         ans_list.append(str(i))

# print(' '.join(ans_list))