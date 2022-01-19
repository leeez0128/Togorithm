import sys
input = sys.stdin.readline


def solution(A, B):
    maxV = max(A, B)
    minV = min(A, B)
    
    while minV > 0:
        temp = minV;
        minV = maxV % minV;
        maxV = temp;
        
    return [maxV, int((A * B) / maxV)]


if __name__ == '__main__':
    A, B = map(int, input().strip().split())
    print(*solution(A, B), sep="\n")
