# 2750. 수 정렬하기
# https://www.acmicpc.net/problem/2750

import sys
from typing import MutableSequence

sys.stdin = open("3-1_2750.txt", "r")

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    
    sort_arr = []
    
    for _ in range(N):
        sort_arr.append(int(sys.stdin.readline()))
    
    bubble_sort(sort_arr)
    
    for i in range(N):
        print(sort_arr[i])