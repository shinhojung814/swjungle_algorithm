# 9012. 괄호
# https://www.acmicpc.net/problem/9012

import sys

sys.stdin = open("3-3_9012.txt", "r")
input = sys.stdin.readline

T = int(input())

str_list = [input().split('\n')[0] for str in range(T)]

for str in str_list:
    num1, num2 = 0, 0
    flag = True
    for char in str:
        if char == '(':
            num1 += 1
        elif char == ')':
            num2 += 1
            if num2 > num1:
                flag = False
                
    if flag == False:
        print('NO')
    else:
        if num1 != num2:
            print('NO')
        else:
            if str.startswith('('):
                if str.endswith(')'):
                    print('YES')