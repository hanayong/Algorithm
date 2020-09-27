import unittest

__author__ = 'hanayong'


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def print_queue(self):
        print(self.items)

    def size(self):
        return len(self.items)


class QueueTest(unittest.TestCase):

    def test(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.size(), 3)
        queue.print_queue()
        queue.dequeue()
        self.assertEqual(queue.size(), 2)
        queue.print_queue()
        queue.dequeue()
        queue.print_queue()
        queue.dequeue()
        self.assertTrue(queue.is_empty())


if __name__ == '__main__':
    QueueTest().test()