# 2751. 수 정렬하기 2
# https://www.acmicpc.net/problem/2751

import sys
from typing import MutableSequence

sys.stdin = open("3-2_2751.txt", "r")

def heap_sort(a):
    
    def down_heap(a, left, right):
        temp = a[left]
        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1
            cr = cl + 1
            child = cr if cr <= right and a[cr] > a[cl] else cl
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp
    
    n = len(a)
    
    for i in range((n - 1) // 2, -1, -1):
        down_heap(a, i, n - 1)
    
    for i in range(n - 1, 0, -1):
        a[0], a[i], = a[i], a[0]
        down_heap(a, 0, i - 1)

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    
    sorted_arr = []
    
    for _ in range(N):
        sorted_arr.append(int(sys.stdin.readline()))
    
    heap_sort(sorted_arr)
    
    for i in range(N):
        print(sorted_arr[i])