# 9663. N-Queen
# https://www.acmicpc.net/problem/9663

import sys

input_num = int(sys.stdin.readline())
# 각 열에서 퀸의 위치
pos = [0] * input_num
# 각 행에 퀸을 배치했는지 체크
flag_row = [False] * input_num
# 대각선1 방향으로 퀸을 배치했는지 체크
flag_diag1 = [False] * (2 * input_num - 1)
# 대각선2 방향으로 퀸을 배치했는지 체크
flag_diag2 = [False] * (2 * input_num - 1)

def put():
    # 각 열에 배치한 퀸의 위치를 출력
    for i in range(input_num):
        print(f'{pos[i]: 2}', end='')
    print()

def set(i: int) -> None:
    # i열의 알맞은 위치에 퀸을 배치
    for j in range(input_num):
        # j행에 퀸을 배치하지 않았으면
        if (not flag_row[j]
            # 대각선1 방향으로 퀸이 배치되지 않았다면
            and not flag_diag1[i + j]
            # 대각선2 방향으로 퀸이 배치되지 않았다면
            and not flag_diag2[i - j + input_num - 1]):
            # 퀸을 j행에 배치
            pos[i] = j
            # 모든 열에 퀸 배치를 완료
            if i == input_num - 1:
                put()
            else:
                flag_row[j] = flag_diag1[i + j] = flag_diag2[i - j + input_num - 1] = True
                # 다음 열에 퀸을 배치
                set(i + 1)
                flag_row[j] = flag_diag1[i + j] = flag_diag2[i - j + input_num - 1] = False

# 0열에 퀸을 배치
set(0)