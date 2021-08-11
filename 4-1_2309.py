# 2309. 일곱 난쟁이
# https://www.acmicpc.net/problem/2309

import sys
from itertools import combinations

sys.stdin = open("4-1_2309.txt", "r")

height_list = []

for _ in range(9):
    height_list.append(int(sys.stdin.readline()))

height_combinations = list(combinations(height_list, 7))

for combination in height_combinations:
    if sum(combination) == 100:
        height_sum = combination

dwarfs = []

for height in height_sum:
    dwarfs.append(height)

dwarfs.sort()

for answer in dwarfs:
    print(answer)