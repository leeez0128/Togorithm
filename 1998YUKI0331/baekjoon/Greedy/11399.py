import sys
input = sys.stdin.readline


def solution(N, P):
    result = 0
    P.sort()

    for i in range(len(P)):
        result += P[i] * (N - i)
    return result


if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))
    print(solution(N, P))
