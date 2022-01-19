import sys
input = sys.stdin.readline


def solution(A, B):
    if A % B == 0:
        return "multiple"
    elif B % A == 0:
        return "factor"
    else:
        return "neither"


if __name__ == '__main__':
    while True:
        A, B = map(int, input().strip().split())
        if A == 0 and B == 0:
            break
        print(solution(A, B))
