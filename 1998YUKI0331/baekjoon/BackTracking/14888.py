import sys
import itertools
input = sys.stdin.readline


def solution(N, Numbers, opNums):
    Max = float('-inf')
    Min = float('inf')

    Ops = sum([[x] * opNums[x] for x in range(len(opNums))], [])
    for i in itertools.permutations(Ops, len(Ops)):
        temp = Numbers[0]
        for opIdx in range(len(i)):
            if i[opIdx] == 0:
                temp += Numbers[opIdx + 1]
            elif i[opIdx] == 1:
                temp -= Numbers[opIdx + 1]
            elif i[opIdx] == 2:
                temp *= Numbers[opIdx + 1]
            elif i[opIdx] == 3:
                if temp < 0 and Numbers[opIdx + 1] > 0:
                    temp = -1 * ((-1 * temp) // Numbers[opIdx + 1])
                else:
                    temp //= Numbers[opIdx + 1]
        Max = max(Max, temp)
        Min = min(Min, temp)

    print(Max, Min, sep="\n")


if __name__ == '__main__':
    N = int(input())
    Numbers = list(map(int, input().split()))
    opNums = list(map(int, input().split()))

    solution(N, Numbers, opNums)
