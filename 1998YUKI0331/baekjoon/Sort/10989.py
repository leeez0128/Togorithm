import sys
input = sys.stdin.readline

cnt = [0] * (10000 + 1)

N = int(input())

for i in range(N):
    A = int(input())
    cnt[A] += 1

for i in range(len(cnt)):
    for _ in range(cnt[i]):
        print(i, end='\n')


"""
이렇게 하면 메모리 초과가 나오는데, N이 최대 10,000,000이라서 ㅇㅅㅇ.
모두 저장해두고 카운팅 하는 거보다는 그냥 입력 하나하나 받으면서 카운팅 해야됨.
import sys
input = sys.stdin.readline


def solution(N, A):  # 계수정렬
    cnt = [0] * (max(A) + 1)
    for i in A:
        cnt[int(i)] += 1

    for i in range(len(cnt)):
        for _ in range(cnt[i]):
            print(i, end='\n')


if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for _ in range(N)]
    solution(N, A)
"""
