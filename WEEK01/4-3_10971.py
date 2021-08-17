# 10971. 외판원 순회 2
# https://www.acmicpc.net/problem/10971

import sys
from itertools import permutations

sys.stdin = open("4-3_10971.txt")

def solution():
    N = int(sys.stdin.readline())
    cost_matrix = []

    for _ in range(N):
        cost_matrix.append(list(map(int, sys.stdin.readline().split())))

    route_list = list(permutations(range(0, N)))

    min_cost = 1000000 * N

    for route in route_list:
        total_cost = 0
        flag = True
        
        for idx in range(0, N - 1):
            travel_cost = cost_matrix[route[idx]][route[idx + 1]]
            
            if travel_cost == 0:
                flag = False
                break
            
            total_cost += travel_cost
        
        if cost_matrix[route[-1]][route[0]] == 0:
            flag = False
            break
        else:
            total_cost += cost_matrix[route[-1]][route[0]]
        
        if flag == False:
            continue
        else:
            if total_cost < min_cost:
                min_cost = total_cost

    print(min_cost)

solution()