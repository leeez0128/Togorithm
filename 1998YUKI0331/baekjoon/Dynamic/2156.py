import sys
input = sys.stdin.readline


def solution(N, A):
    if N == 1:
        return A[0]
    if N == 2:
        return A[0] + A[1]

    dp = [A[0], A[0] + A[1], max(A[0] + A[1], A[0] + A[2], A[1] + A[2])]
    for i in range(3, N):
        dp.append(max(dp[i - 3] + A[i] + A[i - 1], dp[i - 2] + A[i], dp[i - 1]))
    return dp[N - 1]


if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for _ in range(N)]
    print(solution(N, A))
