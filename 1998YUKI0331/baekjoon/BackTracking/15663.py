import sys
input = sys.stdin.readline


def solution(level):
    if level == M:
        print(*result, sep=" ")
        return

    pre = 0
    for i in range(len(A)):
        if check[i] is False and pre != A[i]:
            check[i] = True
            result[level] = A[i]
            pre = A[i]
            solution(level + 1)
            check[i] = False


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    A = sorted(list(map(int, input().split())))

    result = [0] * M
    check = [False] * N

    solution(0)
