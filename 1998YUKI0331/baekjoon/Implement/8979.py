import sys
input = sys.stdin.readline


def solution(N, K, A):
    rank = 1
    for key, value in list(A.items()):
        if key == K:
            continue
        elif value[0] > A[K][0]:
            rank += 1
        elif value[0] == A[K][0] and value[1] > A[K][1]:
            rank += 1
        elif value[1] == A[K][1] and value[1] == A[K][1] and value[2] > A[K][2]:
            rank += 1

    return rank


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    A = {}
    for _ in range(N):
        id, gold, silver, bronze = map(int, input().strip().split())
        A[id] = [gold, silver, bronze]

    print(solution(N, K, A))
