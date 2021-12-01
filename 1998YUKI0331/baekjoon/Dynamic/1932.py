import sys
input = sys.stdin.readline


def solution(N, A):
    for i in range(1, len(A)):
        for j in range(len(A[i])):
            if j == 0:
                A[i][j] += A[i - 1][j]
            elif j == i:
                A[i][j] += A[i - 1][j - 1]
            else:
                A[i][j] += max(A[i - 1][j - 1], A[i - 1][j])
    return max(A[N - 1])


if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, A))
