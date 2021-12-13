import sys
input = sys.stdin.readline


def solution(N):
    cnt = [0] * 10
    for i in N:
        cnt[int(i)] += 1

    sixnine = cnt[6] + cnt[9]
    if sixnine % 2 == 0:
        sixnine = sixnine // 2
    else:
        sixnine = sixnine // 2 + 1
    cnt[6] = sixnine

    return max(cnt[:9])


if __name__ == '__main__':
    N = str(input().strip())
    print(solution(N))
