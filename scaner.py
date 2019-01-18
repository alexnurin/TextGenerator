#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

file = open('input.txt', encoding='utf-8')
f = file.read()
#file.close()
f = f.split()
print(f)
last = '.'
for i in f:
    text = re.compile('[^a-zа-я:.A-ZА-Я]').sub('', i)
    if text == '':
        continue
    path = 'data/' + last + '.txt'
    file_res = open(path, 'a')
    file_res.write(text + '\n')
    if last[-1] == '.':
        file_res = open('data/.txt', 'a')
        file_res.write(text + '\n')
    last = text.format('utf-8')
open('data/' + last + '.txt', 'a').write('')


