import sys
input = sys.stdin.readline


def solution(arr):
    count = 1
    countArr = [1]
    for idx, num in enumerate(arr[1:]):
        if num >= arr[idx]:
            count += 1
        else:
            countArr.append(count)
            count = 1
    countArr.append(count)

    count = 1
    for idx, num in enumerate(arr[1:]):
        if num <= arr[idx]:
            count += 1
        else:
            countArr.append(count)
            count = 1
    countArr.append(count)
    print(max(countArr))


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().strip().split()))

    solution(arr)
