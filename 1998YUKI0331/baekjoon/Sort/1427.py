import sys
input = sys.stdin.readline


def solution(N):
    N.sort(reverse=True)

    return N


if __name__ == '__main__':
    N = list(map(int, input().strip()))
    print(*solution(N), sep="")
