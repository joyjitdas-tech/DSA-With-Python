#Implement stack using list
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "Empty stack! Cannot pop"
        return self.items.pop()

    def top(self):
        if len(self.items) == 0:
            return "Empty stack"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0
s = Stack()

print(s.pop())
s.push(10)
s.push(20)

print(s.pop())   
print(s.top())   
print(s.size())  