import sys
from collections import deque
input = sys.stdin.readline


dX = [-2, -2, -1, -1, 1, 1, 2, 2]
dY = [-1, 1, -2, 2, -2, 2, -1, 1]


def solution(l, graph, curX, curY, desX, desY):
    queue = deque()
    queue.append((curX, curY))
    graph[curX][curY] = 1

    while queue:
        x, y = queue.popleft()
        if x == desX and y == desY:
            return graph[x][y] - 1
        for i in range(8):
            nextX = x + dX[i]
            nextY = y + dY[i]
            if 0 <= nextX < l and 0 <= nextY < l:
                if graph[nextX][nextY] == 0:
                    graph[nextX][nextY] = graph[x][y] + 1
                    queue.append((nextX, nextY))


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        l = int(input())
        graph = [[0] * (l + 1) for _ in range(l + 1)]
        curX, curY = map(int, input().strip().split())
        desX, desY = map(int, input().strip().split())

        print(solution(l, graph, curX, curY, desX, desY))
