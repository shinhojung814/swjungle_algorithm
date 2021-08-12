# 1920. 수 찾기
# https://www.acmicpc.net/problem/1920

import sys
from typing import Sequence, Any

sys.stdin = open("1-1_1920.txt", "r")

N = int(sys.stdin.readline())

input_str = sys.stdin.readline().split('\n')[0]

num_list = list(map(int, input_str.split()))
num_list.sort()

M = int(sys.stdin.readline())

key_list = list(map(int, sys.stdin.readline().split()))\

def binary_search(a, key):
    pl = 0
    pr = len(a) - 1
    
    while pl <= pr:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return 1
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
    return 0

for key in key_list:
    print(binary_search(num_list, key))
