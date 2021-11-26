import sys
input = sys.stdin.readline


def solution(level):  # 중복 순열
    if level == M:
        for i in result:
            print(i, end=" ")
        print()
        return

    for i in range(N):
        if check[i] is False:
            result[level] = list[i]
            solution(level + 1)


if __name__ == '__main__':
    N, M = map(int, input().strip().split())

    list = [i + 1 for i in range(N)]
    result = [0] * M
    check = [False] * N

    solution(0)
