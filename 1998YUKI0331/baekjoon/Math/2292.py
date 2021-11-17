import sys
input = sys.stdin.readline


def solution(A):
    i = 1
    comb = 1
    while i < A:
        i += comb * 6
        comb += 1
    return comb


if __name__ == '__main__':
    A = int(input())
    print(solution(A))
