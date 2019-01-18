from random import randint
from datetime import datetime

file_res = open('output.txt', 'w')
lastG = ''
n = 30
nextBig = 1
newString = 100
print(datetime.time(datetime.now()))
for i in range(n):
    file = open('data/' + lastG + '.txt', 'r')
    textG_all = file.readlines()
    #print(textG_all)
    if len(textG_all) == 0:
        file_res.write('.')
        nextBig = 1
        file = open('data/.txt', 'r')
        textG_all = file.readlines()
    textG = textG_all[randint(1, len(textG_all))-1][:-1]
    if nextBig:
        nextBig = 0
        file_res.write(" " + textG[0].upper() + textG[1:])
    else:
        file_res.write(" " + textG[0].lower() + textG[1:])
    if textG[-1] == '.':
        nextBig = 1
    lastG = textG
    if i % newString == newString - 1:
        file_res.write('\n')
file_res.write('.')
file_res.close()