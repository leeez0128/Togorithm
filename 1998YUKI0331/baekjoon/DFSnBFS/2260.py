import sys
from collections import deque
input = sys.stdin.readline


dX = [-1, 1, 0, 0]
dY = [0, 0, -1, 1]


def solution(N, M, graph, check):
    queue = deque()
    queue.append((0, 0, 0))  # x, y, z(z==0, 안뿌신 / z==1, 뿌신)
    check[0][0][0] = 1

    while queue:
        x, y, z = queue.popleft()
        if x == N - 1 and y == M - 1:
            return check[x][y][z]

        for i in range(4):
            nextX = x + dX[i]
            nextY = y + dY[i]
            if 0 <= nextX < N and 0 <= nextY < M:
                if graph[nextX][nextY] == 0 and check[nextX][nextY][z] == 0:
                    check[nextX][nextY][z] = check[x][y][z] + 1
                    queue.append((nextX, nextY, z))
                if graph[nextX][nextY] == 1 and z == 0:
                    check[nextX][nextY][z + 1] = check[x][y][z] + 1
                    queue.append((nextX, nextY, z + 1))

    return -1


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    graph = [list(map(int, input().strip())) for _ in range(N)]
    check = [[[0] * 2 for _ in range(M)] for _ in range(N)]

    print(solution(N, M, graph, check))
