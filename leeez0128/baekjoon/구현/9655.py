import sys
input = sys.stdin.readline


def solution(N):
    mok = N // 3
    # print(mok)
    turn = N - mok * 3 + mok
    # print(N - mok*3)
    
    if turn % 2 == 0:
        print("CY")
    else:
        print("SK")
        

if __name__ == '__main__':
    N = int(input().strip())
    solution(N)