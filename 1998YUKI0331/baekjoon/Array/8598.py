import sys
input = sys.stdin.readline


def solution(T):
    for i in range(T):
        flagO = False
        accum = 1
        result = 0
        OX = input()
        for j in OX:
            if (j == 'O'):
                if flagO:
                    accum += 1
                    result += accum
                else:
                    result += accum
                    flagO = True
            else:
                flagO = False
                accum = 1
        print(result)


if __name__ == '__main__':
    T = int(input())
    solution(T)
