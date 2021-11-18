import sys
import math
input = sys.stdin.readline


def solution(M, N):
    array = [True for i in range(N + 1)]  # True면 소수, False면 소수 아님
    array[1] = False

    for i in range(2, int(math.sqrt(N)) + 1):
        if array[i] is True:
            j = 2
            while i * j <= N:
                array[i * j] = False
                j += 1

    if len([i for i in range(M, N + 1) if array[i]]) == 0:
        return [-1]

    return [sum([i for i in range(M, N + 1) if array[i]]),
            min([i for i in range(M, N + 1) if array[i]])]


if __name__ == '__main__':
    M = int(input())
    N = int(input())
    print(*solution(M, N), sep="\n")
