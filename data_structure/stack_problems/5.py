"""
BOJ 쇠막대기(Iron bar) problem
"""

__author__ = 'hanayong'

from sys import stdin

stack = []
ans = 0
line = stdin.readline().rstrip()
trans_line = line.replace('()', '0')


def first_way():
    ans = 0
    for i in trans_line:
        if i == '(':
            stack.append(i)
        elif i == ')':
            stack.pop()
            ans += 1
        else:
            ans += len(stack)

    return ans


def second_way():
    standard = 'O'
    ans = 0
    for i in line:
        if i == '(':
            stack.append(i)
            standard= 'O'
        else:
            if standard == 'O':
                stack.pop()
                ans += len(stack)
                standard = 'C'
            else:
                ans += 1
                stack.pop()
    return ans


if __name__ == '__main__':
    print(first_way())
    print(second_way())