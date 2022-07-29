import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())

for test_case in range(1, T + 1):
    card = input()
    
    # list_ = []
    # for i in card:
    #     if card[0] == '-':           
    #         print(f'#{test_case} 0')
    #         break
    #     if card[0] == '1':            
    #         print(f'#{test_case} 0')
    #         break
    #     if card[0] == '2':            
    #         print(f'#{test_case} 0')
    #         break                   # '카드의 첫자리가 ~~ 거나' 라는 조건을 붙이는데 너무 시간을 오래썼음. 일단 if문을 이렇게 쓸게 아닌거같은데....
    #     if card[0] == '7':            
    #         print(f'#{test_case} 0')
    #         break
    #     if card[0] == '8':            
    #         print(f'#{test_case} 0')
    #         break
    #     if i == '-':
    #         continue
    #     else:
    #         list_.append(i)

    # if len(list_) == 16:
    #     print(f'#{test_case} 1')
    # else:
    #     print(f'#{test_case} 0')

    list_ = []
    for i in card:          # 앞에서 미리 list_의 길이를 정해주지 않고가면 뒤에서 헤매게됨
        if i == '-':
            continue
        else:
            list_.append(i)
    dic_start = {'3' : 'o', '4' : 'o', '5' : 'o', '6' : 'o', '9' : 'o'}         #탐색시간을위해 리스트대신 딕셔너리사용
    for i in card:
        if card[0] not in dic_start:
            print(f'#{test_case} 0')
            break
        if len(list_) == 16:
            print(f'#{test_case} 1')            
            break
        else:
            print(f'#{test_case} 0')
            break