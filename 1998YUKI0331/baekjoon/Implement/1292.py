import sys
input = sys.stdin.readline


def solution(A, B):
    tmp, res = [], []
    num = 1
    while len(res) <= B:
        tmp.append([num] * num)
        res = list(sum(tmp, []))
        num += 1

    return sum(res[A - 1 : B])


if __name__ == '__main__':
    A, B = map(int, input().strip().split())
    print(solution(A, B))
