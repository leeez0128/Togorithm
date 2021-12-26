import sys
from collections import deque
input = sys.stdin.readline


dX = [-1, 1, 0, 0, 0, 0]
dY = [0, 0, 1, -1, 0, 0]
dZ = [0, 0, 0, 0, 1, -1]


def solution(M, N, H, A):
    queue = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if A[i][j][k] == 1:
                    queue.append((i, j, k))

    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nextX = x + dX[i]
            nextY = y + dY[i]
            nextZ = z + dZ[i]
            if 0 <= nextX < H and 0 <= nextY < N and 0 <= nextZ < M:
                if A[nextX][nextY][nextZ] == 0:
                    A[nextX][nextY][nextZ] = A[x][y][z] + 1
                    queue.append((nextX, nextY, nextZ))


if __name__ == '__main__':
    M, N, H = map(int, input().strip().split())
    A = [[] for i in range(H)]

    for i in range(H):
        for j in range(N):
            A[i].append(list(map(int, input().split())))

    solution(M, N, H, A)

    unable = False
    max_num = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if A[i][j][k] == 0:
                    unable = True
                max_num = max(max_num, A[i][j][k])

    print(-1 if unable is True else max_num - 1)
