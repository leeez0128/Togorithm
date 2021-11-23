import sys
input = sys.stdin.readline


def solution(N, A):
    A.sort(key=lambda x: (x[1], x[0]))
    for i in A:
        print(*i, sep=" ")


if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    solution(N, A)
