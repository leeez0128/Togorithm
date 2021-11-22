import sys
input = sys.stdin.readline


def solution(N):
    cnt = 0
    number = 666
    while cnt != N:
        if "666" in str(number):
            cnt += 1
        number += 1
    return number - 1


if __name__ == '__main__':
    N = int(input())
    print(solution(N))
