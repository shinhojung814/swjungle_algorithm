# 1181. 단어 정렬
# https://www.acmicpc.net/problem/1181

import sys

sys.stdin = open("3-4_1181.txt", "r")

N = int(sys.stdin.readline())
arr = []

for _ in range(51):
    arr.append([])

for num in range(N):
    str = sys.stdin.readline().split('\n')[0]
    
    if str not in arr[len(str)]:
        arr[len(str)].append(str)
    
    arr[len(str)].sort()
    
for lst in arr:
    if bool(lst) == True:
        for word in lst:
            print(word)