import sys
input = sys.stdin.readline


def solution(N, M, Board):
    result = 19980331
    W_Board = [[0] * M for _ in range(N)]
    B_Board = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            # W로 시작하는 경우
            if i % 2 == 0 and j % 2 == 0 and Board[i][j] != "W":
                W_Board[i][j] += 1
            elif i % 2 == 0 and j % 2 != 0 and Board[i][j] != "B":
                W_Board[i][j] += 1
            elif i % 2 != 0 and j % 2 == 0 and Board[i][j] != "B":
                W_Board[i][j] += 1
            elif i % 2 != 0 and j % 2 != 0 and Board[i][j] != "W":
                W_Board[i][j] += 1

            # B로 시작하는 경우
            if i % 2 == 0 and j % 2 == 0 and Board[i][j] != "B":
                B_Board[i][j] += 1
            elif i % 2 == 0 and j % 2 != 0 and Board[i][j] != "W":
                B_Board[i][j] += 1
            elif i % 2 != 0 and j % 2 == 0 and Board[i][j] != "W":
                B_Board[i][j] += 1
            elif i % 2 != 0 and j % 2 != 0 and Board[i][j] != "B":
                B_Board[i][j] += 1

    for i in range(N - 8 + 1):
        for j in range(M - 8 + 1):
            W_sum = 0
            B_sum = 0
            W_temp = [row[j:j + 8] for row in W_Board[i:i + 8]]
            B_temp = [row[j:j + 8] for row in B_Board[i:i + 8]]
            for idx in range(8):
                W_sum += sum(W_temp[idx])
                B_sum += sum(B_temp[idx])
            if result > min(W_sum, B_sum):
                result = min(W_sum, B_sum)

    return result


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    Board = [str(input()) for _ in range(N)]
    print(solution(N, M, Board))
