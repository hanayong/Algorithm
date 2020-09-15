"""
BOJ 단어 뒤집기2(word flip2) problem
"""

__author__ = 'hanayong'

from sys import stdin

flag = False
word = ''
result = ''
string = list(stdin.readline().rstrip())

for c in string:
    if c == '<':
        flag = True
        result += word
        word = c
    elif c == '>':
        flag = False
        result += word + c
        word = ''
    elif c == ' ':
        result += (word + c)
        word = ''
    else:
        if flag:
            word += c
        else:
            word = c + word

print(result + word)