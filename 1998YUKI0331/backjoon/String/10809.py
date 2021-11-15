import sys
input = sys.stdin.readline


def solution(S):
    cnt = [-1] * 26
    for i in range(len(S)):
        if (cnt[ord(S[i]) - 97] == -1):
            cnt[ord(S[i]) - 97] = i
    return cnt


if __name__ == '__main__':
    S = input().strip()
    print(*solution(S), sep=" ")
