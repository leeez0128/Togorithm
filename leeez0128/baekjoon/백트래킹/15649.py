import sys
from itertools import permutations
input = sys.stdin.readline


def solution(N, M):
    arr = [i for i in range(1, N+1)]
    seq = list(permutations(arr, M))
    for i in range(len(seq)):
        for j in range(len(seq[i])):
            print(seq[i][j], end=" ")
        print()


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    solution(N, M)
