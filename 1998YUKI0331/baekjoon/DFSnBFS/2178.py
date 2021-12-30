import sys
from collections import deque
input = sys.stdin.readline


dX = [-1, 1, 0, 0]
dY = [0, 0, -1, 1]


def solution(N, M, graph, check):
    queue = deque()
    queue.append((0, 0))
    check[0][0] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nextX = x + dX[i]
            nextY = y + dY[i]
            if 0 <= nextX < N and 0 <= nextY < M:
                if graph[nextX][nextY] == 1:
                    graph[nextX][nextY] += graph[x][y]
                    queue.append((nextX, nextY))

    return graph[N - 1][M - 1]


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    check = [[False] * (M) for _ in range(N)]
    graph = []
    for i in range(N):
        graph.append(list(map(int, input().strip())))

    print(solution(N, M, graph, check))
