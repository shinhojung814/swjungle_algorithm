# 2588. 곱셈
# https://www.acmicpc.net/problem/2588

A, B = map(int, input().split())
C = A * B

while B > 0:
    print(A * (B % 10))
    B = B // 10

print(C)