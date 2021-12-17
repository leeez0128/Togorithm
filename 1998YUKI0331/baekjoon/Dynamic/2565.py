import sys
input = sys.stdin.readline


def solution(N, A):
    A.sort()
    dp = [1 for _ in range(N)] 
    
    for i in range(N):
        for j in range(i + 1):
            if A[i][1] > A[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return (N - max(dp))


if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, A))
