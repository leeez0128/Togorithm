import sys
input = sys.stdin.readline


def solution(X):
    dp = [0, 1, 1]

    for i in range(3, X):
        dp.append(float('inf'))
        if (i + 1) % 3 == 0:
            dp[i] = min(dp[i // 3] + 1, dp[i])
        if (i + 1) % 2 == 0:
            dp[i] = min(dp[i // 2] + 1, dp[i])
        dp[i] = min(dp[i - 1] + 1, dp[i])

    return dp[X - 1]


if __name__ == '__main__':
    X = int(input())
    print(solution(X))
