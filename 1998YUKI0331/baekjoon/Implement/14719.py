import sys
input = sys.stdin.readline


def solution(H, W, A):
    arr = [[0] * W for _ in range(H)]

    for i in range(W):
        for a in range(A[i]):
            arr[a][i] = 1

    for i in range(H):
        start = -1
        end = -1
        for j in range(W):
            if arr[i][j] == 1 and start < j and start != -1:
                end = j
                for k in range(start + 1, end):
                    arr[i][k] = 2
                start = end
            elif arr[i][j] == 1:
                start = j

    result = 0
    for i in range(H):
        result += arr[i].count(2)

    return result


if __name__ == '__main__':
    H, W = map(int, input().strip().split())
    A = list(map(int, input().split()))
    print(solution(H, W, A))
