import sys
input = sys.stdin.readline


def getGCD(A, B):
    maxV = max(A, B)
    minV = min(A, B)

    while minV > 0:
        temp = minV
        minV = maxV % minV
        maxV = temp

    return maxV


def solution(N, A):
    A.sort()
    result = []

    gcd = A[1] - A[0]
    for i in range(2, len(A)):
        gcd = getGCD(gcd, (A[i] - A[i - 1]))
    result.append(gcd)

    for i in range(2, int(gcd ** (0.5)) + 1):
        if gcd % i == 0:
            result.append(i)
            if (i ** 2) != gcd:
                result.append(gcd // i)

    return result


if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for _ in range(N)]
    print(*sorted(solution(N, A)), sep=" ")
