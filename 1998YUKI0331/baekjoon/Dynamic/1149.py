import sys
input = sys.stdin.readline


def solution(N, A):
    for i in range(1, len(A)):
        A[i][0] += min(A[i - 1][1], A[i - 1][2])
        A[i][1] += min(A[i - 1][0], A[i - 1][2])
        A[i][2] += min(A[i - 1][0], A[i - 1][1])

    return min(A[N - 1])


if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, A))
