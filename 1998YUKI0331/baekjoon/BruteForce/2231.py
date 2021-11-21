import sys
input = sys.stdin.readline


def solution(N):
    for i in range(1, N):
        if i + sum(map(int, str(i))) == N:
            return i
    return 0


if __name__ == '__main__':
    N = int(input())
    print(solution(N))
