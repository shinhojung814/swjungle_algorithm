# 2798. 블랙잭
# https://www.acmicpc.net/problem/2798

import sys
from itertools import combinations

sys.stdin = open("2798_블랙잭.txt", 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))
sum_arr = list(combinations(cards, 3))

max_sum = 0

for i in sum_arr:
    if (sum(i) > max_sum) & (sum(i) <= M):
        max_sum = sum(i)

print(max_sum)