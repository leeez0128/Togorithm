import sys
input = sys.stdin.readline


def solution(num):
    strArr = list(str(num))
    answer = []
    for i in range(10):
        print(strArr.count(str(i)))


if __name__ == '__main__':
    num = 1
    for i in range(3):
        num *= int(input())
    solution(num)
