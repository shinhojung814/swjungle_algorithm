# 1920. 수 찾기
# https://www.acmicpc.net/problem/1920

import sys

sys.stdin = open("1-1_1920.txt", "r")
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))

M = int(input())
num_list = list(map(int, input().split()))

def binary_search(A, num):
    left = 0
    right = len(A) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == num:
            return 1
        elif A[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for num in num_list:
    print(binary_search(A, num))