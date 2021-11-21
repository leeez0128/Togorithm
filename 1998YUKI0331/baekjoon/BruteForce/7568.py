import sys
input = sys.stdin.readline


def solution(N, XY):
    result = [1] * N
    for i in range(N):
        for j in range(len(XY)):
            if i == j:
                continue
            else:
                if XY[i][0] < XY[j][0] and XY[i][1] < XY[j][1]:
                    result[i] += 1
    return result


if __name__ == '__main__':
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    print(*solution(N, XY), sep=" ")
