import sys
input = sys.stdin.readline


def getFac(x):
    result = 1 
    for i in range(1, x + 1):
        result *= i
    return result


def solution(N, M):
    return getFac(M) // (getFac(N) * getFac(M - N))


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().strip().split())
        print(solution(N, M))
