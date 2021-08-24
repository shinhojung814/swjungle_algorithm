# 2577. 숫자의 개수
# https://www.acmicpc.net/problem/2577

import sys
sys.stdin = open("1-14_2577.txt", "r")

A = int(input())
B = int(input())
C = int(input())

num_list = list(str(A * B * C))

for num in range(10):
    num_count = 0
    for elem in num_list:
        if num == int(elem):
            num_count += 1
    print(num_count)
    
# 다른 풀이 1.

# A = int(input())
# B = int(input())
# C = int(input())

# g = [0] * 10
# a = str(A * B * C)
# for i in a:
#     g[int(i)] += 1

# for gg in g:
#     print(gg)
    
# 다른 풀이 2.

# A = int(sys.stdin.readline())
# B = int(sys.stdin.readline())
# C = int(sys.stdin.readline())
# product = str(A * B * C)
# num_counter = Counter(product)
# for num in range(10):
#     if str(num) not in num_counter.keys():
#         print(0)
#     else:
#         print(num_counter[str(num)])