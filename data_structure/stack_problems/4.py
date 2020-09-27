"""
BOJ 에디터(editor) problem
"""

__author__ = 'hanayong'

from sys import stdin

if __name__ == '__main__':
    l_stack = list(stdin.readline().rstrip())
    r_stack = []
    cnt = int(stdin.readline())

    for cmd in stdin:
        if cmd[0] == 'L' and l_stack:
            r_stack.append(l_stack.pop())

        if cmd[0] == 'D' and r_stack:
            l_stack.append(r_stack.pop())

        if cmd[0] == 'B' and l_stack:
            l_stack.pop()

        if cmd[0] == 'P':
            l_stack.append(cmd[2])

    print(''.join(l_stack+r_stack[::-1]))