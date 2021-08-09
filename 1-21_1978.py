# 1978. 소수 찾기
# https://www.acmicpc.net/problem/1978

import sys
sys.stdin = open("basic_1-21.txt", "r")

N = int(input())
num_list = list(map(int, input().split()))
# print(N, num_list)
prime_count = 0

def prime_number(num):
    if num == 1:
        return False
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    else:
        return True

for num in num_list:
    if prime_number(num) == True:
        prime_count += 1

print(prime_count)