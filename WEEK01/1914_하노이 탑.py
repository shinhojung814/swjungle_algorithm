# 1914. 하노이의 탑
# https://www.acmicpc.net/problem/1914

def hanoi(num, x, y):
    
    if num > 1:
        hanoi(num - 1, x, 6 - x - y)
    
    print(x, y)
    
    if num > 1:
        hanoi(num - 1, 6 - x - y, y)

n = int(input())
move_count = 2 ** n - 1

if n <= 20:
    print(move_count)
    hanoi(n, 1, 3)

if n > 20:
    print(move_count)