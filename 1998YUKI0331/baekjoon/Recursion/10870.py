import sys
input = sys.stdin.readline


def solution(N):
    if N == 0 or N == 1:
        return N
    else:
        return solution(N - 2) + solution(N - 1)


if __name__ == '__main__':
    N = int(input())
    print(solution(N))
