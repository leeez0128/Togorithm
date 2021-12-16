import sys
input = sys.stdin.readline


def solution(N, C, A):
    cnt = {}

    for i in A:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1

    cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
    result = [[x[0]] * x[1] for x in cnt]

    return sum(result, [])


if __name__ == '__main__':
    N, C = map(int, input().strip().split())
    A = list(map(int, input().split()))
    print(*solution(N, C, A), sep=" ")
