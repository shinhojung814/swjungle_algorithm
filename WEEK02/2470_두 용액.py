# 2470. 두 용액
# https://www.acmicpc.net/problem/2470

import sys

sys.stdin = open("1-4_2470.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

left = 0
right = N - 1
answer = 10 ** 10
idx = (0, 0)

while left != right:
    if answer > abs(arr[left] + arr[right]):
        answer = abs(arr[left] + arr[right])
        idx = (left, right)
    
    if arr[left] + arr[right] < 0:
        left += 1
    elif arr[left] + arr[right] > 0:
        right -= 1
    else:
        break

print(arr[idx[0]], arr[idx[1]])