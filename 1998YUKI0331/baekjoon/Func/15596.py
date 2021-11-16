import sys
input = sys.stdin.readline


def solution(a):  # 답은 이 함수 부분만!
    return sum(a)


if __name__ == '__main__':
    a = list(map(int, input().split()))
    print(solution(a))
