import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())
for test_case in range(1, T + 1):
    M = list(map(int, input().split()))

    sum_ = 0

    for i in range(len(M)):
        if i % 2 == 0:  #리스트는 0부터니까  나눠떨어져서 0되는게 홀수자리수임
            sum_ += M[i] * 2
        else:
            sum_ += M[i]

    for i in range(10):
        if (sum_ + i) % 10 == 0:
            print(f'#{test_case} {i}')
            break