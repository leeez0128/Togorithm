import sys
input = sys.stdin.readline


def solution():
    cnt = [0] * 42
    result = 0
    for i in range(10):
        N = int(input())
        cnt[N % 42] += 1
    for i in cnt:
        if (i != 0):
            result += 1
    print(result)


if __name__ == '__main__':
    solution()
