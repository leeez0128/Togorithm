import sys
input = sys.stdin.readline


def solution(N, K, A):
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            if j < A[i - 1][0]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(A[i - 1][1] + dp[i - 1][j - A[i - 1][0]], dp[i - 1][j])

    return max(dp[N])


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, K, A))
