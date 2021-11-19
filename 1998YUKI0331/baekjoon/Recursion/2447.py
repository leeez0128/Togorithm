import sys
input = sys.stdin.readline


# 사실 시간초과 뜸...
def solution(i, j, N):
    if (i // N) % 3 == 1 and (j // N) % 3 == 1:
        print(" ", end="")
    else:
        if N // 3 == 0:
            print("*", end="")
        else:
            solution(i, j, N // 3)


if __name__ == '__main__':
    N = int(input())

    for i in range(N):
        for j in range(N):
            solution(i, j, N)
        print("")
