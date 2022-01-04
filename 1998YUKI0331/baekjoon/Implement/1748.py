import sys
input = sys.stdin.readline


def solution(N):
    result = 0
    length = len(str(N))
    i = 1

    while i != length:
        result += i * (10 ** ((i - 1))) * 9
        i += 1

    result += (N - (10 ** ((length - 1))) + 1) * length

    return result


if __name__ == '__main__':
    N = int(input())
    print(solution(N))
