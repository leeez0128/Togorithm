import sys
input = sys.stdin.readline


def game(N, candy):
    long_candy = 0 # max(long_candy, cnt+1)
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if candy[i][j] == candy[i][j+1]:
                cnt += 1
            else:
                if j is not N-2:
                    cnt = 1
        long_candy = max(long_candy, cnt)
    
    
    print('log~~', long_candy)
    return long_candy


def solution(N, candy):
    trans_candy = [list(x) for x in zip(*candy)]
    print(max(game(N, candy), game(N, trans_candy)))


if __name__ == '__main__':
    N = int(input().strip())
    candy = []
    for _ in range(N):
        candy.append(input().strip())
    solution(N, candy)