import sys
input = sys.stdin.readline


def solution(N, K, A):
    result = 0
    A.sort(reverse=True)
    for i in A:
        if i <= K:
            result += K // i
            K -= i * (K // i)
    return result


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    A = [int(input()) for _ in range(N)]
    print(solution(N, K, A))
