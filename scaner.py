import re


def scaner():
    file = open('input.txt', 'r', encoding='utf-8')
    bigFile = open("names.txt", 'a', encoding='utf-8')
    f = file.read().split()
    file.close()
    nextBig = 1
    if len(f) == 0:
        return
    print(f)
    last = '1'
    reg = re.compile(r'[^a-zа-я:\.?!A-ZА-Я]')
    toOne = re.compile(r'[?!\.]')
    for i in f:
        text = reg.sub('', i)
        text = toOne.sub('1', text).replace('ё', 'е')
        if text == '':
            continue
        print(text)

        if text[0].isupper() and nextBig:
            file_res = open('data/1.txt', 'a')
            file_res.write(text + '\n')
            nextBig = 0
        elif text[0].isupper():
            bigFile.write(text + '\n')
            file_res = open('data/' + last + '.txt', 'a')
            file_res.write(text + '\n')
        else:
            file_res = open('data/' + last + '.txt', 'a')
            file_res.write(text + '\n')
        if text[-1] == '1':
            nextBig = 1
        last = text.format('utf-8')
    open('data/' + last + '.txt', 'a').write('')


scaner()
