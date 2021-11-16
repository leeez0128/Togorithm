import sys
input = sys.stdin.readline


def solution(N):
    for n in range(N):
        cnt = [-1] * 26
        S = input().strip()
        for i in range(len(S)):
            if cnt[ord(S[i]) - 97] != -1 and (i - cnt[ord(S[i]) - 97]) != 1:
                N -= 1
                break
            cnt[ord(S[i]) - 97] = i
    return N


if __name__ == '__main__':
    N = int(input().strip())
    print(solution(N))
