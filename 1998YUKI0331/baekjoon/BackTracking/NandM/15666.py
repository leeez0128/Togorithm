import sys
input = sys.stdin.readline


def solution(level, start):
    if level == M:
        for i in result:
            print(i, end=" ")
        print()
        return

    pre = 0
    for i in range(start, N):
        if check[i] is False and pre != A[i]:
            result[level] = A[i]
            pre = A[i]
            solution(level + 1, i)


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    A = sorted(list(map(int, input().split())))

    result = [0] * M
    check = [False] * N

    solution(0, 0)
