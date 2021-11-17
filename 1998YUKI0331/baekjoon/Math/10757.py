import sys
input = sys.stdin.readline


def solution(A, B):
    return A + B


if __name__ == '__main__':
    A, B = map(int, input().strip().split())
    print(solution(A, B))
