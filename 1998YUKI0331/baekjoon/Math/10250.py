import sys
import math
input = sys.stdin.readline


def solution(T):
    while T > 0:
        H, W, N = map(int, input().strip().split())
        T -= 1
        if N % H == 0:
            print(H * 100 + math.ceil(N / H))
        else:
            print((N % H) * 100 + math.ceil(N / H))


if __name__ == '__main__':
    T = int(input())
    solution(T)
