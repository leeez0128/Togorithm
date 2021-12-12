import sys
input = sys.stdin.readline


def solution(N, A):
    result = 1
    A.sort(key=lambda x: (x[1], x[0]))
    endTime = A[0][1]

    for i in range(1, len(A)):
        if endTime <= A[i][0]:
            endTime = A[i][1]
            result += 1

    return result


if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, A))
