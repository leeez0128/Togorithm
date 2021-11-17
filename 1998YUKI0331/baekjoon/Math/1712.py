import sys
input = sys.stdin.readline


def solution(A, B, C):
    if (B >= C):
        return -1
    return A // (C - B) + 1


if __name__ == '__main__':
    A, B, C = map(int, input().strip().split())
    print(solution(A, B, C))
