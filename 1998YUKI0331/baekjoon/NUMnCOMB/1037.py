import sys
input = sys.stdin.readline


def solution(N, A):
    return max(A) * min(A)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(solution(N, A))
