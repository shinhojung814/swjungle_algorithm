# 1920. 수 찾기
# https://www.acmicpc.net/problem/1920

import sys

sys.stdin = open("1-1_1920.txt", "r")

N = int(sys.stdin.readline())

input_str = sys.stdin.readline().split('\n')[0]

num_list = list(map(int, input_str.split()))
num_list.sort()

M = int(sys.stdin.readline())

key_list = list(map(int, sys.stdin.readline().split()))

for key in key_list:
    start = 0
    end = len(num_list) - 1
    flag = False
    
    while start <= end:
        mid = (start + end) // 2
        if num_list[mid] == key:
            flag = True
            break
        elif num_list[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    if flag == True:
        print(1)
    else:
        print(0)
