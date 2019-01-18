import re


file = open('input.txt', 'r')
f = file.read()
file.close()
print(f)

f = f.lower().split()
print(f)
last = ''
for i in f:
    text = re.compile('[^a-zа-я]').sub('', i)
    path = 'data/' + last + '.txt'
    file_res = open(path, 'a')
    file_res.write(text + '\n')
    print(last, text)
    last = text.format('cp1251')



