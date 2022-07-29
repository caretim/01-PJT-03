import sys

sys.stdin = open("_문자열의거울상.txt")


T = int(input())

for test_case in range(1, T + 1):

    char= input()

    rechar=[]

    for i in char:
        if i =='b':
            i= i.replace('b','d')
            rechar.append(i)
        elif i =='d':
            i= i.replace('d','b')
            rechar.append(i)
        elif i == 'p':
            i= i.replace('p','q')
            rechar.append(i)
        elif i == 'q':
            i= i.replace('q','p')
            rechar.append(i)

    reselt= ''.join(rechar)[::-1]
    
    print(f'#{test_case} {reselt}')
