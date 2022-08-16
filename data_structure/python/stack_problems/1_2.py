"""
BOJ Stack problem
"""

__author__ = 'hanayong'


n = int(input())

for _ in range(n):
    strings = list(map(list, input().split()))
    for i in strings:
        print(''.join(i[::-1]), end=' ')