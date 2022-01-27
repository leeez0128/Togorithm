import sys
input = sys.stdin.readline

def solution(N, M, broken):
    ans = abs(100 - target) 
    for num in range(1000001): 
        for N in str(num):
            if N in broken: 
                break
        else: 
            ans = min(ans, len(str(num)) + abs(num - target))
    print(ans)
if __name__ == '__main__':
    target = int(input())
    M = int(input())
    if M:
        broken = set(input().split())
    else:
        broken = set()
    solution(target,M,broken)