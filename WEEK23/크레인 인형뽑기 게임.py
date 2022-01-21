def solution(board, moves):
    answer = 0
    arr = [[] for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[j][i] != 0:
                arr[i].append(board[j][i])

    result = []

    for k in range(len(moves)):
        index = moves[k] - 1
        item = arr[index][-1]

        if len(result):
            if result[-1] == item:
                result.pop(-1)
                answer += 2
            else:
                result.append(item)
        else:
            result.append(item)
    
    return answer

board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0 ,1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board, moves))