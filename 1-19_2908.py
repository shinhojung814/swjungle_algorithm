# 2908. 상수
# https://www.acmicpc.net/problem/2908

A, B = map(int, input().split())
num1, num2 = 0, 0

while A > 0:
    temp1 = A % 10
    num1 = num1 * 10 + temp1
    A = A // 10

while B > 0:
    temp2 = B % 10
    num2 = num2 * 10 + temp2
    B = B // 10
    
print(max(num1, num2))

# 다른 풀이.

# import sys
# num1, num2 = sys.stdin.readline().split()
# num1 = num1[::-1]
# num2 = num2[::-1]
# print(max(int(num1), int(num2)))