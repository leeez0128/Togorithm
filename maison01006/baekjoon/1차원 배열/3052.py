import sys
input = sys.stdin.readline


def solution(arr):
    answer = {}
    for num in arr:
        answer[num % 42] = 0
    print(len(answer))


if __name__ == '__main__':
    arr = []
    for i in range(10):
        arr.append(int(input()))
    solution(arr)
