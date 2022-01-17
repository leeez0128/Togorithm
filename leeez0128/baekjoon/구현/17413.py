import sys
input = sys.stdin.readline


def solution(S):
    tag = ''
    word = ''
    for i in range(len(S)):
        if S[i] == '<':
            if tag == "":
                tag += S[i]
                continue
            tags = tag.split(" ")
            for arr in tags:
                word += arr[::-1]
                word += " "
            word = word.rstrip()
            tag = ''
            tag += S[i]
        elif S[i] == '>':
            tag += S[i]
            word += tag
            tag = ''

        else:
            tag += S[i]
        
        if i == len(S)-1:
            tags = tag.split(" ")
            for arr in tags:
                word += arr[::-1]
                word += " "
        
    print(word)


if __name__ == '__main__':
    S = input().strip()
    solution(S)
