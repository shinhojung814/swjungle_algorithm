# 4344. 평균은 넘겠지
# https://www.acmicpc.net/problem/4344

import sys
sys.stdin = open("1-13_4344.txt", "r")

for num in range(int(input())):
    input_arr = list(map(int, input().split()))
    N, scores = input_arr[0], input_arr[1:]
    
    avg_score = sum(scores) / N
    good = 0
    
    for student in scores:
        if student > avg_score:
            good += 1
    
    answer = good / N * 100
    print(str("%.3f"%answer) + '%')