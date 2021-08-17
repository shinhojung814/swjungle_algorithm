# 1085. 직사각형에서 탈출
# https://www.acmicpc.net/problem/1085

x, y, w, h = map(int, input().split())

print(min(abs(x - 0), abs(y - 0), abs(w - x), abs(h - y)))