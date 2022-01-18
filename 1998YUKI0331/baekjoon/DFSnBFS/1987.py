"""
틀렸습니다임... 투비 컨티뉴...
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

dX = [-1, 1, 0, 0]
dY = [0, 0, -1, 1]


def solution(x, y, alphabets, cnt):   # DFS
    global result
    result = max(result, len(list(set(alphabets))))
    alphabets.append(graph[x][y])
    print(x, y, alphabets, cnt)

    for i in range(4):
        nextX = x + dX[i]
        nextY = y + dY[i]
        if 0 <= nextX < R and 0 <= nextY < C:
            if graph[nextX][nextY] not in alphabets:
                solution(nextX, nextY, alphabets, cnt + 1)


if __name__ == '__main__':
    R, C = map(int, input().strip().split())
    graph = [list(map(str, input().strip())) for _ in range(R)]
    alphabets = []
    result = 0
    
    solution(0, 0, alphabets, 1)

    print(result)