import sys
input = sys.stdin.readline


def solution(N):
    cnt_0 = [1, 0]
    cnt_1 = [0, 1]
    for i in range(2, N + 1):
        cnt_0.append(cnt_0[i - 1] + cnt_0[i - 2])
        cnt_1.append(cnt_1[i - 1] + cnt_1[i - 2])
    return cnt_0[N], cnt_1[N]


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(*solution(N), sep=" ")
