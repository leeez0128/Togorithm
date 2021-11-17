import sys
input = sys.stdin.readline


def solution(N):
    arr = list(map(lambda x: x // 3 if x % 3 == 0 else 19980331,
                   [i + 1 for i in range(N + 1)]))

    for i in range(5, N + 1):
        if i % 5 == 0:
            arr[i - 1] = min(arr[i - 1], i // 5)
        if arr[i - 5] != 19980331:
            arr[i] = min(arr[i], arr[i - 5] + 1)

    return arr[N - 1] if arr[N - 1] != 19980331 else -1


if __name__ == '__main__':
    N = int(input())
    print(solution(N))
