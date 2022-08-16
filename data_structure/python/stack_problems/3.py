"""
BOJ 스택 수열(stack sequence) problem
"""

__author__ = 'hanayong'

from sys import stdin

n = int(stdin.readline())
n_list = map(lambda x: int(x.rstrip()), stdin.readlines())


def func():
    cnt, stack, result = 1, [], []

    for i in n_list:
        while cnt <= i:
            stack.append(cnt)
            result.append('+')
            cnt += 1
        if stack.pop() != i:
            return 'NO'
        else:
            result.append('-')

    return '\n'.join(result)


print(func())