import sys
input = sys.stdin.readline


result = []
def solution(x):
    if x == 0:
        if len(result) == 0:
            print(0)
            return
        result.sort()
        print(result.pop())
    elif x > 0:
        result.append(x)


if __name__ == '__main__':
    N = int(input().strip())
    for _ in range(N):
        x = int(input().strip())
        solution(x)
