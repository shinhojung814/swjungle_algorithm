def solution(location, s, e):
    answer = 0

    x_min, x_max = min(s[0], e[0]), max(s[0], e[0])
    y_min, y_max = min(s[1], e[1]), max(s[1], e[1])

    for unit in location:
        if x_min <= unit[0] <= x_max and y_min <= unit[1] <= y_max:
            answer += 1

    return answer

location = [[0, 3], [1, 1], [1, 5], [2, 2], [3, 3], [4, 0]]
s, e = [1, 4], [4, 1]
print(solution(location, s, e))

location = [[0, 3], [1, 1], [1, 5], [2, 2], [3, 3], [4, 0]]
s, e = [3, 4], [0, 0]
print(solution(location, s, e))