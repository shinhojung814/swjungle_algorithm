# 10872. 팩토리얼
# https://www.acmicpc.net/problem/10872

import math

def factorial(N):
    if N > 0:
        return N * factorial(N - 1)
    else:
        return 1

print(factorial(N = int(input())))