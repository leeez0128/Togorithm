import sys
input = sys.stdin.readline


def solution(N, A):
    A.sort(key=lambda x: int(x[0]))
    for i in A:
        print(i[0], i[1])


if __name__ == '__main__':
    N = int(input())
    A = [list(map(str, input().split())) for _ in range(N)]
    solution(N, A)
