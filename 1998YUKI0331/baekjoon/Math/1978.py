import sys
import math
input = sys.stdin.readline


def solution(N, A):
    for i in A:
        if i == 1:
            N -= 1
        for num in range(2, int(math.sqrt(i)) + 1):
            if i % num == 0:
                N -= 1
                break
    return N


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(solution(N, A))
