import sys
import itertools
input = sys.stdin.readline


def calc(X, opNum, Y):
    if opNum == 0:
        return X + Y
    elif opNum == 1:
        return X - Y
    elif opNum == 2:
        return X * Y
    elif opNum == 3:
        if X < 0 and Y > 0:
            return -1 * ((-1 * X) // Y)
        else:
            return X // Y


def solution(N, Numbers, opNums):
    Max = float('-inf')
    Min = float('inf')

    Ops = sum([[x] * opNums[x] for x in range(len(opNums))], [])
    for i in itertools.permutations(Ops, len(Ops)):
        temp = 0
        for opIdx in range(len(i)):
            if opIdx == 0:
                temp = calc(Numbers[0], i[opIdx], Numbers[1])
            else:
                temp = calc(temp, i[opIdx], Numbers[opIdx + 1])
        Max = max(Max, temp)
        Min = min(Min, temp)

    print(Max, Min, sep="\n")


if __name__ == '__main__':
    N = int(input())
    Numbers = list(map(int, input().split()))
    opNums = list(map(int, input().split()))

    solution(N, Numbers, opNums)
