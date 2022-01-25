import sys
input = sys.stdin.readline


def solution(N, M, arr):
    min_length = min(N,M)
    answer=0
    for i in range(N):
        for j in range(M):
            for k in range(min_length):
                if ((i+k)<N) and((j+k)<M) and(arr[i][j]==arr[i][j+k]==arr[i+k][j]==arr[i+k][j+k]):
                    answer = max(answer,(k+1)**2)
    print(answer)
if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    arr = []
    for i in range(N):
        arr.append(list(input()))
    solution(N,M,arr)
