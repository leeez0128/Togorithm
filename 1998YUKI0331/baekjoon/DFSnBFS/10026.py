import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


dX = [-1, 1, 0, 0]
dY = [0, 0, -1, 1]


def dfs(x, y, A, check, N):  # dfs, bfs 둘다 연습하려고 2개 따로 짬
    check[x][y] = True

    for i in range(4):
        nextX = x + dX[i]
        nextY = y + dY[i]
        if 0 <= nextX < N and 0 <= nextY < N:
            if A[x][y] == A[nextX][nextY] and check[nextX][nextY] is False:
                dfs(nextX, nextY, A, check, N)


def bfs(x, y, A, check, N):
    queue = deque()
    queue.append((x, y))
    check[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nextX = x + dX[i]
            nextY = y + dY[i]
            if 0 <= nextX < N and 0 <= nextY < N:
                if A[x][y] == A[nextX][nextY] and check[nextX][nextY] is False:
                    queue.append((nextX, nextY))
                    check[nextX][nextY] = True


if __name__ == '__main__':
    N = int(input())
    A = [list(map(str, input().strip())) for _ in range(N)]

    result = 0
    check = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if check[i][j] is False:
                dfs(i, j, A, check, N)
                result += 1
    print(result, end=" ")

    result = 0
    check = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        A[i] = ["R" if x == "G" else x for x in A[i]]
    for i in range(N):
        for j in range(N):
            if check[i][j] is False:
                bfs(i, j, A, check, N)
                result += 1
    print(result)
