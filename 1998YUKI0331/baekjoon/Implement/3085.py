import sys
input = sys.stdin.readline


def get_max(N, A):
    result_row, result_col = 1, 1
    for i in range(N):
        cnt_row, cnt_col = 1, 1
        for j in range(1, N):
            if A[i][j] == A[i][j - 1]:
                cnt_row += 1
            else:
                cnt_row = 1
            result_row = max(result_row, cnt_row)

            if A[j][i] == A[j - 1][i]:
                cnt_col += 1
            else:
                cnt_col = 1
            result_col = max(result_col, cnt_col)

    return max(result_row, result_col)


def get_exchange_max(N, A):
    result = get_max(N, A)

    for i in range(N):
        for j in range(1, N):
            if A[i][j - 1] != A[i][j]:
                A[i][j - 1], A[i][j] = A[i][j], A[i][j - 1]
                result = max(result, get_max(N, A))
                A[i][j - 1], A[i][j] = A[i][j], A[i][j - 1]

            if A[j - 1][i] != A[j][i]:
                A[j - 1][i], A[j][i] = A[j][i], A[j - 1][i]
                result = max(result, get_max(N, A))
                A[j - 1][i], A[j][i] = A[j][i], A[j - 1][i]

    return result


if __name__ == '__main__':
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(str, input().strip())))

    print(get_exchange_max(N, A))
