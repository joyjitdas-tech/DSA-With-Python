#Implement Queue using Stack
class queueBystack:
    def __init__(self):
        self.st1 = []
        self.st2 = []
    def enqueue(self,val):
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(val)
        while self.st2:
            self.st1.append(self.st2.pop())

    def deque(self):
        if len(self.st1) == 0:
            return "empty queue"
        x = self.st1.pop()
        return x
    def front(self):
        if len(self.st1) == 0:
            return "empty queue"
        return self.st1[-1]
    def rear(self):
        if len(self.st1) == 0:
            return "e,pty queue"
        return self.st1[0]
    def is_empty(self):
        return len(self.st1) == 0
    def size(self):
        return len(self.st1)
    

q = queueBystack()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)

print(q.st1)
print(q.rear())
print(q.front())
q.deque()
q.deque()
print(q.st1)