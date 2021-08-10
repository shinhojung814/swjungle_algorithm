# 2908. 상수
# https://www.acmicpc.net/problem/2908

import sys

A, B = sys.stdin.readline().split()

num1 = int(A[::-1])
num2 = int(B[::-1])
    
print(max(num1, num2))