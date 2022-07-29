import sys

sys.stdin = open("_직사각형길이찾기.txt")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num =[]
    num=list(map(int,input().split()))


    if num[0] == [num[1]] and num[1] ==num[3]:
        print(f'#{test_case} {num[0]}')
    elif num[0] == num[1]:
        print(f'#{test_case} {num[2]}')
    elif num[1] == num[2]:
        print (f'#{test_case} {num[0]}')
    elif num [2] == num[0]:
        print (f'#{test_case} {num[1]}')