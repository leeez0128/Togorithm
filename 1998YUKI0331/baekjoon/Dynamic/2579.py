import sys
input = sys.stdin.readline


def solution(N, A):
    dp = []
    if N <= 2:
        return sum(A)
    dp.append(A[0])
    dp.append(max(A[1], A[0] + A[1]))
    dp.append(max(A[0] + A[2], A[1] + A[2]))

    for i in range(3, len(A)):
        dp.append(max(dp[i - 2] + A[i], dp[i - 3] + A[i - 1] + A[i]))
    return dp[N - 1]


if __name__ == '__main__':
    N = int(input())
    A = [int(input().strip()) for _ in range(N)]
    print(solution(N, A))
