import sys
input = sys.stdin.readline


def solution(A, B, V):
    return (V - B - 1) / (A - B) + 1


if __name__ == '__main__':
    A, B, V = map(int, input().strip().split())
    print(int(solution(A, B, V)))
