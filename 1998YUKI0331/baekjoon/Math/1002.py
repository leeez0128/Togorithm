import sys
import math
input = sys.stdin.readline


def solution(T):
    while T > 0:
        T -= 1
        A = list(map(int, input().split()))

        distance = math.sqrt((A[0] - A[3]) ** 2 + (A[1] - A[4]) ** 2)

        if A[2] + A[5] < distance:
            print(0)
        elif abs(A[2] - A[5]) > distance:
            print(0)
        elif distance == 0 and A[2] == A[5]:
            print(-1)
        elif A[2] + A[5] == distance:
            print(1)
        elif abs(A[2] - A[5]) == distance:
            print(1)
        else:
            print(2)


if __name__ == '__main__':
    T = int(input())
    solution(T)
