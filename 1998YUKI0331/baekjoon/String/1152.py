import sys
input = sys.stdin.readline


def solution(S):
    result = S.split()
    return len(result)


if __name__ == '__main__':
    S = input().strip()
    print(solution(S))
