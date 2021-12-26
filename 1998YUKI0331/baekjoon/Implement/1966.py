import sys
from collections import deque
input = sys.stdin.readline


def solution(N, doc, que):
    idx = deque(list(range(N)))
    cnt = 0
    while que:
        if que[0] == max(que):
            cnt += 1
            que.popleft()
            if idx.popleft() == doc:
                return cnt
        else:
            que.append(que.popleft())
            idx.append(idx.popleft())


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N, doc = map(int, input().strip().split())
        que = deque(list(map(int, input().split())))
        print(solution(N, doc, que))
