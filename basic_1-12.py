# 8958. OX퀴즈
# https://www.acmicpc.net/problem/8958

import sys
sys.stdin = open("basic_1-12.txt", "r")

for num in range(int(input())):
    board = list(map(str, input()))
    total_score = 0
    score = 0
    for result in board:
        if result == 'O':
            score += 1
            total_score += score
        else:
            score = 0
    print(total_score)