import sys
input = sys.stdin.readline


def solution(S):
    split_S = S.split('-')
    nums = []

    for i in split_S:
        tmp = 0
        if '+' not in i:
            nums.append(int(i))
        else:
            split_i = i.split('+')
            for j in split_i:
                tmp += int(j)
            nums.append(int(tmp))

    result = nums[0]
    result -= sum(nums[1:])
    return result


if __name__ == '__main__':
    S = str(input().strip())
    print(solution(S))
