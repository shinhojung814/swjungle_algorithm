# 1269. 대칭 차집합
# https://www.acmicpc.net/problem/1269

import sys

sys.stdin = open("1269_대칭 차집합.txt", 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# print(len(A - B) + len(B - A))
print(len(set(A) ^ set(B)))