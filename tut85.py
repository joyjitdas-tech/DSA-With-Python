#Implement Stack using Queue
from collections import deque

class stackByQueue:
    def __init__(self):
        self.queue = deque()

    def push(self,value):
        self.queue.append(value)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if len(self.queue) == 0:
            return "empty stack"
        x = self.queue.popleft()
        return x
    def top(self):
        if len(self.queue) == 0:
            return "stack is empty"
        return self.queue[0]
    def is_empty(self):
        return (self.queue) == 0
    def size(self):
        return len(self.queue)
    
s = stackByQueue()

print(s.pop())
s.push(10)
s.push(20)
s.push(70)
s.push(30)
s.push(50)

print(s.pop())   
print(s.top())   
print(s.pop())   
print(s.size())  