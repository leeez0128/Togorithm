import sys
input = sys.stdin.readline


def check(lev):  # 가로, 대각선 확인하는 콜백 함수
    for i in range(lev):
        if board[lev] == board[i] or abs(board[lev] - board[i]) == lev - i:
            return False
    return True


def solution(N, level):
    global result

    if level == N:
        result += 1
        return

    for i in range(N):
        board[level] = i
        if check(level):
            solution(N, level + 1)


if __name__ == '__main__':
    N = int(input())
    board = [0] * N

    result = 0
    solution(N, 0)
    print(result)
