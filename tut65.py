#Doubbly Linked List
class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class DoubblyLL:
    def __init__(self):
        self.head = None
    #inserting node in LL at head
    def insert_at_head(self,val):
        new = Node(val)
        if self.head == None:
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
    #append -> insert at last
    def append(self,val):
        new = Node(val)
        if self.head == None:
            self.head = new
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new
            new.prev = temp

    #inserting in between by position given
    def insert_at_btw(self,val,position):
        new = Node(val)
        if position == 0:
            self.insert_at_head(val)
            return
        else:
            temp = self.head
            count = 0
            while count < position -1 and temp:
                temp = temp.next
                count+=1
            if temp is None:
                print("positon out of bound")
                return
            new.next = temp.next
            new.prev = temp
            if temp.next:
                temp.next.prev = new
            temp.next = new
            
    #traverse and print
    def traverse(self):
        curr = self.head
        while curr is not None:
            print("eliment is",curr.val)
            curr = curr.next
    
    #delete at head
    def del_at_head(self):
        if self.head is None:
            print("list is empty")
            return
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None




#create
dll = DoubblyLL()

#append nodes
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)
dll.append(60)

print("After append:")
dll.traverse()

# #insert at head
# dll.insert_at_head(5)

# print("After insert at head:")
# dll.traverse()

# #insert in between
# dll.insert_at_btw(15,2)

# print("After insert at position 2:")
# dll.traverse()

# #delete head
# dll.del_at_head()

# print("After deleting head:")
# dll.traverse()

#creating a func to reverse
def reverse(dll):
    curr = dll.head
    last = None
    if curr.next is None:
        return curr
    while curr is not None:
        front = curr.next
        curr.next = last
        curr.prev = front
        
        last = curr
        curr = front
    dll.head = last

reverse(dll)
print("after reverse")
dll.traverse()