import sys
input = sys.stdin.readline


def solution(N, M, A):
    result = 0

    for num in range(1, max(N, M) + 1):
        for i in range(N - num + 1):
            for j in range(M - num + 1):
                temp = [row[j:j + num] for row in A[i:i + num]]  # 정사각형으로 슬라이스
                if temp[0][0] == temp[0][len(temp) - 1] == temp[len(temp) - 1][0] == temp[len(temp) - 1][len(temp) - 1]:
                    result = max(result, len(temp) * len(temp))

    return result


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    A = [list(map(int, input().strip())) for _ in range(N)]
    print(solution(N, M, A))
