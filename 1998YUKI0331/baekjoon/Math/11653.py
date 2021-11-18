import sys
input = sys.stdin.readline


def solution(N):
    i = 2
    result = []
    while N != 1:
        if N % i == 0:
            N = N / i
            result.append(i)
        else:
            i += 1
    return result


if __name__ == '__main__':
    N = int(input())
    print(*solution(N), sep="\n")
