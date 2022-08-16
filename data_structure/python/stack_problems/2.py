"""
BOJ 괄호 problem
"""

__author__ = 'hanayong'


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        standard = 0
        ps = list(input())
        for i in ps:
            if i == '(':
                standard += 1
            else:
                standard -= 1
            if standard < 0:
                print('NO')
                break
        if standard > 0:
            print('NO')
        elif standard == 0:
            print('YES')