import sys
input = sys.stdin.readline


def solution(A, B, C):
    if B+C >= 60:
        if (B+C)%60 == 0:
            minutes = 0
        else:
            minutes = (B+C) - ((B+C)//60 * 60)
        if A == 23:
            print(0, minutes)
        else:
            print(A+((B+C)//60), minutes)
    else:
        if A == 23:
            print(0, B+C)
        else:
            print(A, B+C)


if __name__ == '__main__':
    A, B = map(int, input().strip().split())
    C = int(input().strip())
    solution(A, B, C)
