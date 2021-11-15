import sys
input = sys.stdin.readline


def solution(S):
    croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    for i in croatia:
        S = S.replace(i, "#")
    return len(S)


if __name__ == '__main__':
    S = input().strip()
    print(solution(S))
