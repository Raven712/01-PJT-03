import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())
for i in range(1, T + 1):
    num = int(input())
    list_ = list(map(int, input().split()))
    dic_list = {}
    for j in list_:
        if j not in dic_list:
            dic_list[j] = 1
        else:
            dic_list[j] = dic_list[j] + 1
    ans = max(dic_list, key = dic_list.get)   ## 어제 배운것.. 딕셔너리에서 키의 밸류 최대값인 키를 출력하는법
    print(f'#{i} {ans}')