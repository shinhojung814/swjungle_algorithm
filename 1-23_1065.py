# 1065. 한수
# https://www.acmicpc.net/problem/1065

import sys
sys.stdin = open("basic_1-23.txt", "r")

for num in range(4):
    input_num = input()
    # print(input_num)

    if int(input_num) < 100:
        num_count = int(input_num)
        print(num_count)
    else:
        num_count = 99
        for num in range(100, int(input_num) + 1):
            num_diff1 = int(str(num)[1]) - int(str(num)[0])
            num_diff2 = int(str(num)[2]) - int(str(num)[1])
            if num_diff1 == num_diff2:
                num_count += 1
            else:
                continue
        print(num_count)
        
# input_num = int(input())
# num_count = 0

# if input_num < 100:
#     num_count = input_num
# else:
#     for num in range(101, num+1):
#         if num < 100:
#             num_count += 1

# print(num_count)