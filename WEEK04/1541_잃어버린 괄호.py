# 1541. 잃어버린 괄호
# https://www.acmicpc.net/problem/1541

import sys

sys.stdin = open("1541_잃어버린 괄호.txt", "r")
input = sys.stdin.readline

str = input().rstrip()
result = []

for item in str.split('-'):
    item = item.lstrip('0')
    if '+' in item:
        item = '(' + item + ')'
    result.append(item)

result = "-".join(result)

print(eval(result))

# for char in result:
#     if type(char) != int:
#         result = result.split(char)

# print(result)