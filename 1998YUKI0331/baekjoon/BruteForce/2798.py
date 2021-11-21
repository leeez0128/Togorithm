import sys
from itertools import combinations
input = sys.stdin.readline


def solution(N, M, A):
    min = 19980331
    for i in combinations(A, 3):
        if M - sum(i) >= 0 and M - sum(i) < min:
            min = M - sum(i)
            result = sum(i)
    return result


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    A = list(map(int, input().split()))
    print(solution(N, M, A))
