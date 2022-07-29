import sys

sys.stdin = open("_암호문1.txt")

N = int(input())

second = list(map(int,input().split()))

third = int(input())

fourth = list(input().split())

x = []
y = []
s = []
where = []
for i in range(len(fourth)):
    if fourth[i] == 'I':
        x.append(fourth[i + 1])
        y.append(fourth[i + 2])
        where.append(i + 3)

for i in range(len(where)):
    if i != len(where) - 1:
        for j in range(where[i], where[i + 1] - 3):
            s.append(fourth[j])                        #s에 4번째 입력된것들의 I ,x, y 가 아닌 숫자들만 순서대로 담음
    if i == len(where) - 1:
        for k in range(where[i-1], len(fourth) + 1):
            s.append(fourth[k])
            

count = 0
sum_y = 0
sum_y_l = []
for i in y:
    sum_y += int(i)
    sum_y_l.append(sum_y)
print(s)