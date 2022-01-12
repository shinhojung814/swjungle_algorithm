import sys

sys.stdin = open("10828_스택.txt", "r")
input = sys.stdin.readline

N = int(input())

orders = [input().split() for _ in range(N)]
print(orders)

stack = []

for order in orders:
    if order[0] == 'push':
        stack.append(order[1])
    if order[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if order[0] == 'size':
        print(len(stack))
    if order[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    if order[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)