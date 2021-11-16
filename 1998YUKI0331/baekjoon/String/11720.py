import sys
input = sys.stdin.readline


def solution():
    # ValueError: invalid literal for int() with base 10: '\n' 땜에 input 대신 아래처럼
    result = sum(map(int, sys.stdin.readline().rstrip()))
    return result


if __name__ == '__main__':
    N = int(input())
    print(solution())
