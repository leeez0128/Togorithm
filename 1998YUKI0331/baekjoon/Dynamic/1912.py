import sys
input = sys.stdin.readline


def solution(N, A):
    dp = [A[0]]
    for i in range(1, N):
        dp.append(max(dp[i - 1] + A[i], A[i]))

    return max(dp)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(solution(N, A))
