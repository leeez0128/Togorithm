import sys
input = sys.stdin.readline


def solution(N):
    global dp

    if N == 0 or N == 1:
        return N
    if dp[N] != 0:
        return dp[N]
    dp[N] = solution(N - 1) + solution(N - 2)
    return dp[N]


if __name__ == '__main__':
    T = int(input())
    dp = [0] * 41

    for _ in range(T):
        N = int(input())
        if N == 0:
            print("1 0")
        else:
            print(solution(N - 1), solution(N))
