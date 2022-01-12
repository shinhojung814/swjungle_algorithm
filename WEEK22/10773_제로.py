import sys

sys.stdin = open("10773_제로.txt", "r")
input = sys.stdin.readline

K = int(input())
stack = []

for i in range(K):
    num = int(input())
    
    if num == 0:
        if stack:
            stack.pop()
    else:
        stack.append(num)

if stack:
    print(sum(stack))
else:
    print(0)