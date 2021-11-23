import sys
input = sys.stdin.readline


def solution(N, A):
    cnt = {}
    sum = 0
    for i in A:
        sum += i
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    frq = sorted(cnt.values(), reverse=True)
    frq_key = [key for key, value in cnt.items() if value == frq[0]]

    result = []
    A.sort()
    frq_key.sort()

    result.append(int(round(sum/N, 0)))
    result.append(A[N // 2])
    if len(frq_key) > 1:
        result.append(frq_key[1])
    else:
        result.append(frq_key[0])
    result.append(max(A) - min(A))

    return result


if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for _ in range(N)]
    print(*solution(N, A), sep="\n")
