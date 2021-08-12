# 2869. 달팽이는 올라가고 싶다
# https://www.acmicpc.net/problem/2869

import sys
import math
sys.stdin = open("1-20_2869.txt", "r")

for num in range(3):
    A, B, V = map(int, input().split())
    # print(A, B, V)

    day_count = (V - B) / (A - B)

    print(math.ceil(day_count))
    # print(day_count)