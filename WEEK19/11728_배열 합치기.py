# 11728. 배열 합치기
# https://www.acmicpc.net/problem/11728

import sys

sys.stdin = open("11728_배열 합치기.txt", 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*sorted(A + B))