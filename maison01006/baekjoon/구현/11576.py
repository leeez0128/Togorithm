import sys
import math
input = sys.stdin.readline


def solution(A, B, m, A_nums):
    num = 0
    answer = []
    A_nums.reverse()

    for x in range(m-1, -1, -1):
        num += (A_nums[x]*(math.pow(A, x)))

    while num != 0:
        answer.append(int(num % B))
        num //= B
    answer.reverse()
    for x in answer:
        print(x)


if __name__ == '__main__':
    A, B = map(int, input().strip().split())
    m = int(input().strip())
    A_nums = list(map(int, input().strip().split()))
    solution(A, B, m, A_nums)
