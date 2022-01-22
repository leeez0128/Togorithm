import sys
input = sys.stdin.readline


def solution(arr):
    print(max(arr), arr.index(max(arr))+1)


if __name__ == '__main__':
    arr = []
    for i in range(9):
        arr.append(int(input()))
    solution(arr)
