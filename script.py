# coding: utf-8
from random import randint

char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0',
             '1', '2', '3', '4', '5', '6', '7', '8', '9',
             '#', '$', '%', '&', '*', '_', '(', ')', '-']

password = ''

for i in range(10):
    pos = randint(0, len(char_list)-1)
    password = password + char_list[pos]

print(f'Password: \033[1;32m {password} \033[m')
