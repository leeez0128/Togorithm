import sys
input = sys.stdin.readline


def solution():
    while True:
        try:
            A, B = map(int, input().strip().split())
            print(A + B)
        except Exception:
            break


if __name__ == '__main__':
    solution()
