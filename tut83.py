#implement of queue by list
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if len(self.items) == 0:
            return "empty queue"
        x = self.items.pop(0)
        return x
    def size(self):
        return len(self.items)
    def is_empty(self):
        return len(self.items) == 0
    def front(self):
        if len(self.items) == 0:
            return "empty queue"
        return self.items[0]
    def rear(self):
        if len(self.items) == 0:
            return "empty queue"
        return self.items[-1]
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())  
print(q.front())    
print(q.rear())     