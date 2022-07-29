import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    N_list = list(map(int, input().split()))  # 리스트의 요소개수는 N개, 각각은 1~10만사이 수

    def average(A):
        sum_A = 0
        for i in A:         #평균구하는함수가 내장된지 모르겠지만 일단 만들었음
            sum_A += i
        return sum_A / len(A)
    
    count = 0
    for i in N_list:
        if average(N_list) >= i:
            count += 1
    print(f'#{test_case} {count}')


