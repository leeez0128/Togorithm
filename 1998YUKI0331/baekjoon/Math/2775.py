import sys
input = sys.stdin.readline


def solution(T):
    while T > 0:
        T -= 1
        k = int(input())
        n = int(input())
        list = [i + 1 for i in range(n)]  # 0층 사는 사람들

        for i in range(1, k):
            for idx in range(1, len(list)):
                list[idx] += list[idx - 1]

        print(sum(list))


if __name__ == '__main__':
    T = int(input())
    solution(T)
