import sys
input = sys.stdin.readline


def RowCheck(x, val):
    for i in range(9):
        if val == sudoku[x][i]:
            return False
    return True


def ColCheck(y, val):
    for i in range(9):
        if val == sudoku[i][y]:
            return False
    return True


def RecCheck(x, y, val):
    nextX = x // 3 * 3
    nextY = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if val == sudoku[nextX + i][nextY + j]:
                return False
    return True


def solution(level):
    if level == len(blanks):
        for i in range(9):
            print(*sudoku[i])
        sys.exit(0)   # 이거 없어서 계속 오답이었따..
        # 없거나 return이면 모든 스도쿠의 답을 출력하지만
        # exit(0)은 강제 종료라 하나만 출력.
        # 모든 칸이 빈칸인 스도쿠 같은 테케에서 오답 처리 됐나부다.
    for i in range(1, 10):
        nextX = blanks[level][0]
        nextY = blanks[level][1]

        if RowCheck(nextX, i) and ColCheck(nextY, i) and RecCheck(nextX, nextY, i):
            sudoku[nextX][nextY] = i
            solution(level + 1)
            sudoku[nextX][nextY] = 0  # 재귀 내부에서 정답 없을 경우


if __name__ == '__main__':
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    blanks = [[i, j] for i in range(9) for j in range(9) if sudoku[i][j] == 0]
    solution(0)
