import sys
from collections import deque
input = sys.stdin.readline


dX = [-1, 1, 0, 0]
dY = [0, 0, -1, 1]


def solution(N, M, A):
    queue = deque()
    for i in range(N):
        for j in range(M):
            if A[i][j] == 1:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nextX = x + dX[i]
            nextY = y + dY[i]
            if 0 <= nextX and nextX < N and 0 <= nextY and nextY < M:
                if A[nextX][nextY] == 0:
                    A[nextX][nextY] = A[x][y] + 1
                    queue.append((nextX, nextY))


if __name__ == '__main__':
    M, N = map(int, input().strip().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    solution(N, M, A)

    unable = False
    for i in A:
        if 0 in i:
            unable = True

    print(-1 if unable is True else max(map(max, A)) - 1)
