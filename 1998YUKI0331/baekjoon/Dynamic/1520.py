import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dX = [-1, 1, 0, 0]
dY = [0, 0, -1, 1]


def dfs(x, y, N, M, A, dp):
    if x == N - 1 and y == M - 1:
        return 1
    dp[x][y] = 0

    for i in range(4):
        nextX = x + dX[i]
        nextY = y + dY[i]
        if 0 <= nextX < N and 0 <= nextY < M:
            if A[x][y] > A[nextX][nextY]:
                if dp[nextX][nextY] >= 0:  # 방문했을 경우는 루프 안돌아
                    dp[x][y] += dp[nextX][nextY]
                else:
                    dp[x][y] += dfs(nextX, nextY, N, M, A, dp)
    return dp[x][y]


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[-1 for _ in range(M)] for _ in range(N)]

    print(dfs(0, 0, N, M, A, dp))
