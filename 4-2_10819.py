# 10819. 차이를 최대로
# https://www.acmicpc.net/problem/10819

import sys
from itertools import permutations

sys.stdin = open("4-2_10819.txt", "r")

N = int(sys.stdin.readline())
input_arr = list(map(int, sys.stdin.readline().split()))

cases = list(permutations(input_arr, N))

max_sum = 0

for i in cases:
    arr = list(i)
    diff_sum = 0

    for idx in range(0, len(arr) - 1):
        diff_sum += abs(arr[idx] - arr[idx + 1])
        
        if diff_sum > max_sum:
            max_sum = diff_sum 

print(max_sum)