# 1316. 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

import sys

sys.stdin = open("1316_그룹 단어 체커.txt", "r")
input = sys.stdin.readline

N = int(input())
result = N

for i in range(N):
    word = input()
    for j in range(0, len(word) - 1):
        if word[j] == word[j + 1]:
            pass
        elif word[j] in word[j + 1:]:
            result -= 1
            break

print(result)