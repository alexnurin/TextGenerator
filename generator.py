from random import randint
from datetime import datetime
from params import *

file_res = open('output.txt', 'w')
lastG = '1'

print(datetime.time(datetime.now()))
for i in range(n):
    file = open('data/' + lastG + '.txt', 'r')
    textG_all = file.readlines()
    if len(textG_all) == 0:
        file = open('data/1.txt', 'r')
        textG_all = file.readlines()
    textG = textG_all[randint(1, len(textG_all)) - 1][:-1]
    file_res.write(" " + textG.replace('1', '.'))
    lastG = textG
    if textG[-1] == '1':
        lastG = '1'
    if i % newString == newString - 1:
        file_res.write('\n')
file_res.write('.')
file_res.close()
