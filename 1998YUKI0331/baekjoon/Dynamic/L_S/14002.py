import sys
input = sys.stdin.readline


def solution(N, A):
    dp = [1 for _ in range(N)]
    LIS = []

    for i in range(N):
        LIS.append([])
        for j in range(i + 1):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        start = dp[i]
        for j in range(i, -1, -1):
            if start == dp[j]:
                LIS[i].append(A[j])
                start -= 1

    print(max(dp))
    print(*reversed(LIS[dp.index(max(dp))]), sep=" ")


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    solution(N, A)
