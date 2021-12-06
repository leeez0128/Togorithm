import sys
input = sys.stdin.readline


def solution(N):
    dp = [1, 2]
    for i in range(2, N):
        dp.append((dp[i - 2] + dp[i - 1]) % 15746)

    return dp[N - 1]


if __name__ == '__main__':
    N = int(input())
    print(solution(N))