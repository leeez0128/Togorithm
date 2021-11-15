import sys
input = sys.stdin.readline


def solution():
    max = -1
    idx = 1
    for i in range(9):
        N = int(input())
        if (max < N):
            max = N
            idx = i + 1
    print(max, idx, sep="\n")


if __name__ == '__main__':
    solution()
