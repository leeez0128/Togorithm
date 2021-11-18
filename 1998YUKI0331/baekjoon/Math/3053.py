import sys
import math
input = sys.stdin.readline


def solution(R):
    return ['{:.6f}'.format(round(R ** 2 * math.pi, 6)),
            '{:.6f}'.format(R ** 2 * 2)]


if __name__ == '__main__':
    R = int(input())
    print(*solution(R), sep="\n")
