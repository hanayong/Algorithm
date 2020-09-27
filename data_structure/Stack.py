class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            print(self.items.pop())
        else:
            print(-1)

    def stack_size(self):
        print(len(self.items))

    def is_empty(self):
        if len(self.items) < 0:
            print(1)
        else:
            print(0)

    def print_top(self):
        if len(self.items) > 0:
            print(self.items[-1])
        else:
            print(-1)
    
 
