import sys

sys.stdin = open("_문자열의거울상.txt")


T = int(input())
for test_case in range(1, T + 1):
    word = input()   #길이 1~1000, bdpq만 씀

    word_dic = {
        'b' : 'd',
        'd' : 'b',
        'p' : 'q',
        'q' : 'p'
    }  # 리스트를 안쓴건 혹시나 시간문제가 생길까봐 딕셔너리를 쓰기로함
    list_word = list(word)

    for i in range(len(word)):
        if list_word[i] in word_dic:
            list_word[i] = word_dic[word[i]]

    list_word = list_word[::-1]
    print(f'#{test_case}', end =' ')
    for i in range(len(list_word)):                 # 시간을 줄이려고 위에서 딕셔너리를 썼는데 for에 if를 중첩시켜서 O(N^2)가 된게 아쉽다. 다른방법이 있었을지도
        if i == len(list_word) - 1:
            print(list_word[i])
        else:
            print(list_word[i], end = '')