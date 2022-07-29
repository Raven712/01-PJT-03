import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())
for test_case in range(1, T + 1):
    length = list(map(int, input().split()))

    count = {}
    for i in length:
        if i not in count:
            count[i] = 1
        else:
            count[i] = count[i] + 1
    
    for i in length:
        if count[i] == 1:                   # 그냥 별로 안어려움 (규칙찾기가 쉬웠음. 구현하기도 쉬웠음.)
            print(f'#{test_case} {i}')
            break
        if count[i] == 3:
            print(f'#{test_case} {i}')
            break