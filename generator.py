from random import randint


file_res = open('output.txt', 'w')
last = u''
n = 300
for i in range(n):
    file = open('data/' + last + '.txt', 'r')
    text_all = file.readlines()
    print(text_all)
    if len(text_all) == 0:
        file_res.write('.')
        file = open('data/.txt', 'r')
        text_all = file.readlines()
    text = text_all[randint(1, len(text_all))-1][:-1]
    file_res.write(" " + text)
    last = text
    if i % 20 == 19:
        file_res.write('\n')
