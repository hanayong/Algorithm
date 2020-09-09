"""
BOJ Stack problem
"""

__author__ = 'hanayong'

stack = []


def push(word):
    global stack

    for _ in range(len(word)):
        stack.append(word.pop())


def pop():
    global stack

    if stack in []:
        return
    else:
        return stack.pop()


def reserve_words():
    global stack
    word_list = []
    for _ in range(len(stack)):
        word_list.append(pop()[::-1])
    print(' '.join(word_list))


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        factors = input().split()
        push(factors)
        reserve_words()