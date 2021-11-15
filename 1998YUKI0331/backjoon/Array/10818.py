import sys
input = sys.stdin.readline


def solution(N, A):
    print(min(A), max(A))
    # 사실 입력받을 때 비교하는게 제일 빠르지겠지만... ~


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    solution(N, A)
