import sys
input = sys.stdin.readline


def solution(X):
    dp = [[0] * 10 for _ in range(101)]  # dp[n][i]: n자리 이며 i로 끝나는 계단수
    dp[0] = list(map(lambda x: 1 if x != 0 else 0, range(10)))

    for n in range(1, X):
        dp[n][0] = dp[n - 1][1]
        dp[n][9] = dp[n - 1][8]
        for i in range(1, 9):
            dp[n][i] = dp[n - 1][i - 1] + dp[n - 1][i + 1]

    return sum(dp[X - 1]) % 1000000000


if __name__ == '__main__':
    X = int(input())
    print(solution(X))
