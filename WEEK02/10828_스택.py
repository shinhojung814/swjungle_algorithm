# 10828. 스택
# https://www.acmicpc.net/problem/10828

# push X: 정수 X를 스택에 넣는 연산
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력
# size: 스택에 들어있는 정수의 개수를 출력
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력. 만약 스택에 들어있는 정수가 없는 경우 -1을 출력.

import sys

sys.stdin = open("3-1_10828.txt", "r")
input = sys.stdin.readline

N = int(input())

input_arr = [input().split('\n')[0] for i in range(N)]
stack = []

for str in input_arr:
    if str.split()[0] == 'push':
        stack.append(str.split()[1])
    elif str == 'pop':
        if len(stack) != False:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif str == 'size':
        print(len(stack))
    elif str == 'empty':
        if len(stack) == False:
            print(1)
        else:
            print(0)
    elif str == 'top':
        if len(stack) != False:
            print(stack[-1])
        else:
            print(-1)