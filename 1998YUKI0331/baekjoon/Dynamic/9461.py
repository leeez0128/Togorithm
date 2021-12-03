import sys
input = sys.stdin.readline


def solution(N):
    dp = [1, 1, 1]
    for i in range(3, N):
        dp.append(dp[i - 2] + dp[i - 3])

    return dp[N - 1]


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solution(N))
