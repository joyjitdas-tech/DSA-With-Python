# Implement Stack & Queue using Doubly Linked List 
class Node:
    def __init__(self,data):
        self.data = data
        self.next  = None
        self.prev = None
#for stack push from front side
class StackDLL:
    def __init__(self):
        self.tail = None  #top

    def push(self, val):
        new_node = Node(val)

        if not self.tail:
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def pop(self):
        if not self.tail:
            return "Stack empty"

        val = self.tail.data

        if self.tail.prev is None:   # only one element
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return val
    def top(self):
        if not self.tail:
            return "Stack is empty"
        return self.tail.data
    def display(self):
        if not self.tail:
            print("Stack is empty")
            return

        temp = self.tail
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("None")
class QueueDLL:
    def __init__(self):
        self.head = None  # front
        self.tail = None  # rear

    def enqueue(self, val): 
        new_node = Node(val)

        if not self.tail:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def dequeue(self):  
        if not self.head:
            return "Queue empty"

        val = self.head.data
        self.head = self.head.next

        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        # updating tail when last element is removed
        return val
    def front(self):
        if not self.head:
            return "empty queue"
        return self.head.data
    def rear(self):
        if not self.head:
            return "queue is empty"
        return self.tail.data
    def display(self):
        if not self.head:
            print("Queue is empty")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


stack1 = StackDLL()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
stack1.push(6)
stack1.pop()
stack1.display()

queue = QueueDLL()
queue.enqueue(11)
queue.enqueue(12)
queue.enqueue(13)
queue.enqueue(14)
queue.enqueue(15)
queue.enqueue(16)
queue.dequeue()
queue.display()