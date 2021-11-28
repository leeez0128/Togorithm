import sys
input = sys.stdin.readline


def solution(level, idx):
    global min
    if level == N // 2:
        Link = [x for x in range(N) if x not in Start]
        startScore = 0
        linkScore = 0

        for i in range(N // 2):
            for j in range(N // 2):
                startScore += S[Start[i]][Start[j]]
                linkScore += S[Link[i]][Link[j]]

        if abs(startScore - linkScore) < min:
            min = abs(startScore - linkScore)

        return

    for i in range(idx, N):
        Start[level] = i
        solution(level + 1, i + 1)


if __name__ == '__main__':
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    Start = [0] * (N // 2)
    min = 19980331

    solution(0, 0)
    print(min)
