import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline
result = []
already = []


def BackTracking(seq, use, M):
    if len(result) == M:
        if str(result) not in already:
            print(*result)
            already.append(str(result))
            return
    
    for num in range(len(seq)):
        if not use[num]:
            result.append(seq[num])
            use[num] = True
            BackTracking(seq, use, M)
            result.pop()
            use[num] = False


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    seq = sorted(list(map(int, input().strip().split())))
    use = [False]*N
    BackTracking(seq, use, M)