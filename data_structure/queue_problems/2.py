"""
BOJ 요세푸스 순열(Josephus permutation) problem
"""

__author__ = 'hanayong'


from sys import stdin

# 1 <= K <= N <= 5,000
N, K = list(map(int, stdin.readline().split()))
n_list = list(range(1, N+1))
result = []
control = K - 1

for _ in range(N):
    if len(n_list) > control:
        result.append(n_list.pop(control))
        control += K - 1

    elif len(n_list) <= control:
        control = control % len(n_list)
        result.append(n_list.pop(control))
        control += K - 1

print('<', end='')
for i in result:
    if i == result[-1]:
        print(i, end='')
        break
    print(i, end=', ')
print('>', end='')