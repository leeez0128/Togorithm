import sys
input = sys.stdin.readline


def solution(N, A):
    A = list(set(A))
    A.sort(key=lambda x: (len(x), x))
    return A


if __name__ == '__main__':
    N = int(input())
    A = [str(input().strip()) for _ in range(N)]
    print(*solution(N, A), sep="\n")
