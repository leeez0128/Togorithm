import sys
input = sys.stdin.readline


def Set(N):  # https://studyandwrite.tistory.com/325
    S = 0
    for _ in range(N):
        op = input().split()  # 메모리초과 오류로 인해 입력받고 바로 출력

        if op[0] == 'add':
            S |= (1 << int(op[1]))
        elif op[0] == 'remove':
            S &= ~(1 << int(op[1]))
        elif op[0] == 'check':
            print(1 if S & (1 << int(op[1])) != 0 else 0)
        elif op[0] == 'toggle':
            S ^= (1 << int(op[1]))
        elif op[0] == 'all':
            S = (1 << 21) - 1
        elif op[0] == 'empty':
            S = 0


if __name__ == '__main__':
    N = int(input())
    Set(N)
