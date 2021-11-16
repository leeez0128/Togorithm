import sys
input = sys.stdin.readline


def solution(A, B, C):
    cnt = [0] * 10
    for i in str(A * B * C):
        cnt[int(i)] += 1
    for i in cnt:
        print(i)


if __name__ == '__main__':
    A = int(input())
    B = int(input())
    C = int(input())
    solution(A, B, C)
