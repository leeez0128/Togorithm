import sys
input = sys.stdin.readline


def solution(N, A):
    sortedA = sorted(list(set(A)))
    # return list(map(lambda x: sortedA.index(x), A))
    # list.index는 O(N)이라서 시간초과 ㅠㅠ
    dic = {}
    for i in range(len(sortedA)):
        dic[sortedA[i]] = i

    return list(map(lambda x: dic[x], A))


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(*solution(N, A), sep=" ")
