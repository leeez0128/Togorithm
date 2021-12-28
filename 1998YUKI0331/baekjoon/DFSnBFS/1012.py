import sys
from collections import deque
input = sys.stdin.readline


dX = [-1, 1, 0, 0]
dY = [0, 0, -1, 1]


def solution(graph, check, M, N, x, y):
    queue = deque()
    queue.append((x, y))
    check[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nextX = x + dX[i]
            nextY = y + dY[i]
            if 0 <= nextX < N and 0 <= nextY < M:
                if graph[nextX][nextY] == 1 and check[nextX][nextY] == False:
                    check[nextX][nextY] = True
                    queue.append((nextX, nextY))


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().strip().split())
        graph = [[0] * M for _ in range(N)]
        check = [[False] * M for _ in range(N)]
        count = 0

        for _ in range(K):
            X, Y = map(int, input().strip().split())
            graph[Y][X] = 1

        for i in range(N):
            for j in range(M):
                if graph[i][j] == 1 and check[i][j] == False:
                    solution(graph, check, M, N, i, j)
                    count += 1

        print(count)
