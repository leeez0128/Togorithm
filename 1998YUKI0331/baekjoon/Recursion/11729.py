import sys
input = sys.stdin.readline


def solution(N, start, to, via):
    if N == 1:
        print(start, to)
    else:
        solution(N - 1, start, via, to)
        print(start, to)
        solution(N - 1, via, to, start)


if __name__ == '__main__':
    N = int(input())
    print(2 ** N - 1)
    solution(N, 1, 3, 2)
