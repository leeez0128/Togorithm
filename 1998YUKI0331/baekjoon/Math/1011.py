import sys
import math
input = sys.stdin.readline


def solution(T):
    while T > 0:
        T -= 1
        x, y = map(int, input().strip().split())

        if int((y - x) ** 0.5) ** 2 == (y - x):  # 완전제곱수이면,
            print(int(math.sqrt(y - x) + (math.sqrt(y - x) - 1)))
        else:
            distance = y - x
            while int(distance ** 0.5) ** 2 != distance:
                distance -= 1
            print(int(math.sqrt(distance) + round(math.sqrt(y - x), 0)))


if __name__ == '__main__':
    T = int(input())
    solution(T)
