import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dX = [-1, 1, 0, 0, -1, -1, 1, 1]
dY = [0, 0, -1, 1, -1, 1, -1, 1]


"""
def solution(x, y, w, h, graph):   # BFS
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nextX = x + dX[i]
            nextY = y + dY[i]
            if 0 <= nextX and nextX < h and 0 <= nextY and nextY < w:
                if graph[nextX][nextY] == 1:
                    graph[nextX][nextY] = 0
                    queue.append((nextX, nextY))
"""


def solution(x, y, w, h, graph):   # DFS
    graph[x][y] = 0

    for i in range(8):
        nextX = x + dX[i]
        nextY = y + dY[i]
        if 0 <= nextX and nextX < h and 0 <= nextY and nextY < w:
            if graph[nextX][nextY] == 1:
                graph[nextX][nextY] = 0
                solution(nextX, nextY, w, h, graph)


if __name__ == '__main__':
    while True:
        w, h = map(int, input().strip().split())
        if w == 0 and h == 0:
            break
        graph = [list(map(int, input().split())) for _ in range(h)]
        result = 0

        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    result += 1
                    solution(i, j, w, h, graph)

        print(result)
