# 11053. 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053

import sys

sys.stdin = open("1-5_11053.txt", "r")
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

# N개의 모든 수열의 길이는 1부터 시작하기 때문에
lengths = [1] * N

for i in range(1, N):
    for j in range(i):
        if (A[i] > A[j]) and (lengths[i] < lengths[j] + 1):
            lengths[i] = lengths[j] + 1

print(max(lengths))