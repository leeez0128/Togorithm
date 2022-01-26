import re
import sys
input = sys.stdin.readline


def getFac(x):
    result = 1 
    for i in range(1, x + 1):
        result *= i
    return result


def solution(N):
    result = 0
    for i in str(getFac(N))[::-1]:
        if i != '0':
            break
        result += 1
    
    return result


if __name__ == '__main__':
    N = int(input())
    print(solution(N))
