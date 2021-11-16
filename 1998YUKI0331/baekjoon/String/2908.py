import sys
input = sys.stdin.readline


def solution(A, B):
    return max(int(A[::-1]), int(B[::-1]))


if __name__ == '__main__':
    A, B = map(str, input().strip().split())
    print(solution(A, B))
