import sys
input = sys.stdin.readline


def solution(A, B, m, num_A):
    result = []
    num_10 = 0

    for i in range(len(num_A)):
        num_10 += A ** (m - (i + 1)) * num_A[i]

    while num_10 > 0:
        result.append(num_10 % B)
        num_10 //= B

    return reversed(result)


if __name__ == '__main__':
    A, B = map(int, input().strip().split())
    m = int(input())
    num_A = list(map(int, input().split()))
    print(*solution(A, B, m, num_A), sep=" ")
