import sys
input = sys.stdin.readline


def solution(N, A):
    dp_i = [1 for _ in range(N)]
    dp_d = [1 for _ in range(N)]
    dp_b = [0 for _ in range(N)]

    reversedA = list(reversed(A))

    for i in range(N):
        for j in range(i):
            if A[i] > A[j]:
                dp_i[i] = max(dp_i[i], dp_i[j] + 1)
            if reversedA[i] > reversedA[j]:
                dp_d[i] = max(dp_d[i], dp_d[j] + 1)

    for i in range(N):
        dp_b[i] = dp_i[i] + dp_d[N - i - 1] - 1

    return max((max(dp_b)), max(dp_i), max(dp_d))


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(solution(N, A))
