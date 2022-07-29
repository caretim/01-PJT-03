import sys

sys.stdin = open("_암호문1.txt")

for test_case in range(1, 11):

    n_ori_len =int(input())

    ori_num=[]
    ori_num=list(map(str,input().split()))

    n_oder =int(input())

    oder_list=[]
    oder_list=list(map(str,input().split()))

    rnum = []

    for i in range(len(oder_list)):
        if oder_list[i] == 'I':
            x= int(oder_list[i+1])
            y= int(oder_list[i+2])
            rnum.append(oder_list[i+3:i+3+y]) 
            cnt=0
            for j in rnum[0]:
                ori_num.insert(x+cnt,j)
                cnt+=1
            rnum.clear()

    reselt_list =[]
    for reselt in range(0,10):
        reselt_list.append(str(ori_num[reselt]))
    r=' '.join(reselt_list)
    print(f'#{test_case} {r}')


