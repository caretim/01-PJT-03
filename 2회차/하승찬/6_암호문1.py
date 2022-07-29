import sys

sys.stdin = open("_암호문1.txt")
n_ori_len =int(input())

ori_num=[]
ori_num=list(map(int,input().split()))

n_oder =int(input())

oder_list=[]
oder_list=list(map(str,input().split()))

rnum = []

for i in range(len(oder_list)):
    if oder_list[i] == 'I':
        x= int(oder_list[i+1])
        y= int(oder_list[i+2])
        rnum.append(oder_list[i+3:i+3+y]) 
        for j in rnum[0]:
            ori_num.insert(x,j)
        rnum.clear()
print(ori_num)

