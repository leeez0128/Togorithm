import sys
input = sys.stdin.readline


def solution(N, K, A):
    dp = [0] * (K + 1)
    dp[0] = 1

    for i in A:
        for j in range(i, K + 1):
            dp[j] += dp[j - i]

    return dp[K]


if __name__ == '__main__':
    N, K= map(int, input().strip().split())
    A = [int(input()) for _ in range(N)]
    print(solution(N, K, A))
