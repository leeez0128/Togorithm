import sys
input = sys.stdin.readline


def solution(S):
    A = []
    temp = ""
    tag = 0    # <로 시작했는지(1) 안했는지(0)

    for i in S:
        if i == "<":
            if temp != "":
                A.append(temp)
            temp = ""
            tag = 1

        elif tag == 1 and temp[-1] == ">":
            A.append(temp)
            temp = ""
            tag = 0

        temp += i

        if tag != 1 and temp[-1] == " ":
            A.append(temp)
            temp = ""

    A.append(temp)

    for i in range(len(A)):
        if "<" not in A[i] and " " in A[i]:
            A[i] = A[i][:-1][::-1] + " "
        elif "<" not in A[i] and " " not in A[i]:
            A[i] = A[i][::-1]

    return A


if __name__ == '__main__':
    S = input().strip()
    print(*solution(S), sep="")
