import sys
input = sys.stdin.readline


def solution():
    num = [0] * 10001
    for i in range(10000):
        sum = i
        for j in str(i):
            sum += int(j)
        if sum <= 10000:
            num[sum] += 1

    for idx in range(len(num)):
        if num[idx] == 0:
            print(idx)


if __name__ == '__main__':
    solution()
