import sys
input = sys.stdin.readline


def solution(S1, S2):
    result = 0
    dp = [[0] * (len(S1) + 1) for _ in range((len(S2) + 1))]

    for i in range(1, len(S2) + 1):
        for j in range(1, len(S1) + 1):
            if S2[i - 1] == S1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 0
            result = max(result, dp[i][j])

    return result


if __name__ == '__main__':
    S1 = input().strip()
    S2 = input().strip()
    print(solution(S1, S2))
