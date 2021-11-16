import sys
input = sys.stdin.readline


def solution(T):
    for i in range(T):
        A, B = map(int, input().strip().split())
        print("Case #{}: {} + {} = {}".format(i + 1, A, B, A + B))


if __name__ == '__main__':
    T = input()
    solution(int(T))
