import sys
input = sys.stdin.readline


def solution(X):
    dp = [0, 1, 1]  # dp[i]: (i + 1)이 1이 되려면 몇번?

    for i in range(3, X):
        dp.append(float('inf'))
        if (i + 1) % 3 == 0:
            dp[i] = min(dp[i // 3] + 1, dp[i])
        if (i + 1) % 2 == 0:
            dp[i] = min(dp[i // 2] + 1, dp[i])
        dp[i] = min(dp[i - 1] + 1, dp[i])

    OneToNum = dp[X - 1] - 1
    print(OneToNum + 1)

    while X != 0:
        if X % 3 == 0 and dp[(X // 3) - 1] == OneToNum:
            print(X, end=" ")
            X = X // 3
        elif X % 2 == 0 and dp[(X // 2) - 1] == OneToNum:
            print(X, end=" ")
            X = X // 2
        else:
            print(X, end=" ")
            X = X - 1
        OneToNum -= 1


if __name__ == '__main__':
    X = int(input())
    solution(X)
