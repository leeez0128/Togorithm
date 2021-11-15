import sys
input = sys.stdin.readline


def solution(N):
    A = list(map(int, input().split()))
    M = max(A)
    result = 0
    for i in A:
        result += i / M * 100
    print(result / N)


if __name__ == '__main__':
    N = int(input())
    solution(N)
