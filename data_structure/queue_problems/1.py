"""
BOJ 큐(Queue) problem
"""

__author__ = 'hanayong'

from sys import stdin


if __name__ == '__main__':
    n = int(stdin.readline())
    Queue = []

    for _ in range(n):
        cmd = stdin.readline().split()

        if cmd[0] == 'push':
            Queue.append(cmd[1])

        elif cmd[0] == 'pop':
            if len(Queue) == 0:
                print(-1)
            else:
                print(Queue.pop(0))

        elif cmd[0] == 'size':
            print(len(Queue))

        elif cmd[0] == 'empty':
            if len(Queue) == 0:
                print(1)
            else:
                print(0)

        elif cmd[0] == 'front':
            if len(Queue) == 0:
                print(-1)
            else:
                print(Queue[0])

        elif cmd[0] == 'back':
            if len(Queue) == 0:
                print(-1)
            else:
                print(Queue[-1])