import sys
input = sys.stdin.readline


def solution(S):
    flag = False
    tag = ''
    word = ''
    for i in range(len(S)):
        if S[i] == '<':
            tag += S[i]
            flag = True
        elif S[i] == '>' and flag == True:
            tag += S[i]
            word += tag
            tag = ''
            flag = False
        
        elif flag == True:
            tag += S[i]

        elif flag == False:
            if S[i] == " ":
                tag += S[i]
                word += tag
                tag = ""
            else:
                tag = S[i] + tag

    print(word + tag)


if __name__ == '__main__':
    S = input().strip()
    solution(S)
