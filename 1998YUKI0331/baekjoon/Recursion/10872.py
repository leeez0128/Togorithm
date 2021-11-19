import sys
input = sys.stdin.readline


def solution(N):
    if N == 0 or N == 1:
        return 1
    else:
        return solution(N - 1) * N


if __name__ == '__main__':
    N = int(input())
    print(solution(N))
