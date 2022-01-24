import sys
input = sys.stdin.readline


def getGCD(A, B):
    while B > 0:
        A, B = B, A % B
    return A


def solution(N, A):
    for i in range(1, len(A)):
        print(A[0] // getGCD(A[0], A[i]), "/", A[i] // getGCD(A[0], A[i]), sep="")


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    solution(N, A)
