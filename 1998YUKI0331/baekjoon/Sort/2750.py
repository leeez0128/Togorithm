import sys
input = sys.stdin.readline


def solution(N, A):
    A.sort()
    return A


if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for _ in range(N)]
    print(*solution(N, A), sep="\n")
