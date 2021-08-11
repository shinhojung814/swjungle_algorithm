# 10989. 수 정렬하기 3
# https://www.acmicpc.net/problem/10989

import sys

sys.stdin = open("3-3_10989.txt", "r")

N = int(sys.stdin.readline())

arr = [0] * 10001

for _ in range(N):
    arr[int(sys.stdin.readline())] += 1

for num in range(10001):
    if arr[num] != False:
        for i in range(arr[num]):
            print(num)