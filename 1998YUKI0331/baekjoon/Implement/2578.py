import sys
input = sys.stdin.readline


def check(num, A):
    for i in range(5):
        for j in range(5):
            if num == A[i][j]:
                A[i][j] = 0


def bingo(A):
    bingos = 0

    for i in range(5):     
        cnt1, cnt2 = 0, 0
        for j in range(5):
            if A[i][j] == 0:   # 가로에 빙고 있나 확인
                cnt1 += 1
            if A[j][i] == 0:   # 세로에 빙고 있나 확인
                cnt2 += 1
        if cnt1 == 5:
            bingos += 1
        if cnt2 == 5:
            bingos += 1

    cnt1, cnt2 = 0, 0
    for i in range(5):     # 대각선 빙고 있나 확인
        if A[i][i] == 0:
            cnt1 += 1
        if A[i][4 - i] == 0:
            cnt2 += 1
        if cnt1 == 5:
            bingos += 1
        if cnt2 == 5:
            bingos += 1

    return bingos


def solution(A, N):
    result = 0
    for i in range(5):
        for j in range(5):
            result += 1
            check(N[i][j], A)
            if bingo(A) >= 3:
                return result


if __name__ == '__main__':
    A = [list(map(int, input().split())) for _ in range(5)]
    N = [list(map(int, input().split())) for _ in range(5)]
    print(solution(A, N))
