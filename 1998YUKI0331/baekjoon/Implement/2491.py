import sys
input = sys.stdin.readline


def solution(N, A):
    dp_I = [1 for _ in range(N)]  # 증가하는 수열 최대 길이
    dp_D = [1 for _ in range(N)]  # 작아지는 수열 최대 길이

    for i in range(1, N):
        if A[i] >= A[i - 1]:
            dp_I[i] = dp_I[i - 1] + 1
        if A[i] <= A[i - 1]:
            dp_D[i] = dp_D[i - 1] + 1

    return max(max(dp_I), max(dp_D))


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(solution(N, A))
