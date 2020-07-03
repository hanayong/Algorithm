class stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return not self.items
    
 
stk = stack()      
print(stk)           
print(stk.isEmpty())   
stk.push(1)          
stk.push(2)          
print(stk.pop())     
print(stk.pop())     
print(stk.isEmpty()) 
