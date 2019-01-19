import re

n = 40
bigSet = {i for i in re.compile('[^a-zа-яA-ZА-Я:. \n]').sub('', open("names.txt", 'r', encoding='utf-8').read()).split()}
newString = 15