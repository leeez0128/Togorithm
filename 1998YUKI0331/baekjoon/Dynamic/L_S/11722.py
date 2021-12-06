import sys
input = sys.stdin.readline


def solution(N, A):
    dp = [1 for _ in range(N)]  # dp[i]: A[i]가 마지막 원소일 때 LDS

    for i in range(N):
        for j in range(i + 1):
            if A[i] < A[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(solution(N, A))
