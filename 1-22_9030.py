# 9030. 골드바흐의 추측
# https://www.acmicpc.net/problem/9020

import sys

sys.stdin = open("1-22_9030.txt", "r")

ch = [0] * (10000 + 1)
prime_list = []

for i in range(2, 10000 + 1):
    if ch[i] == 0:
        prime_list.append(i)
        for j in range(i, 10000 + 1, i):
            ch[j] = 1

for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())

    for i in range(num // 2, num + 1):
        if i in prime_list:
            if (num - i) in prime_list:
                print(num - i, i)
                break