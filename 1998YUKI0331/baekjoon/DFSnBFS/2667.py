import sys
from collections import deque
input = sys.stdin.readline


dX = [-1, 1, 0, 0]
dY = [0, 0, -1, 1]


def solution(N, A, x, y):
    queue = deque()
    queue.append((x, y))
    A[x][y] = 0  # 방문하면 0으로 바꿔
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nextX = x + dX[i]
            nextY = y + dY[i]
            if 0 <= nextX and nextX < N and 0 <= nextY and nextY < N:
                if A[nextX][nextY] == 1:
                    A[nextX][nextY] = 0
                    queue.append((nextX, nextY))
                    count += 1
    return count


if __name__ == '__main__':
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().strip())))

    result = []

    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                result.append(solution(N, A, i, j))

    print(len(result))
    print(*sorted(result), sep="\n")
