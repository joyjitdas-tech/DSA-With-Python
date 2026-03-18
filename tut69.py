# Remove Duplicates from a Sorted Doubly Linked List 
#Doubbly Linked List
class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class DoubblyLL:
    def __init__(self):
        self.head = None

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
    #traverse and print
    def traverse(self):
        curr = self.head
        while curr is not None:
            print("eliment is",curr.val)
            curr = curr.next
#create
dll = DoubblyLL()

#append nodes
dll.append(1)
dll.append(1)
dll.append(4)
dll.append(4)
dll.append(5)
dll.append(6)
dll.append(6)
dll.append(9)
dll.append(9)

print("After append:")
dll.traverse()

def remove_duplicate(dll):
    curr = dll.head
    while curr is not None:
        if curr.prev == None:
            curr = curr.next
        if curr.val == curr.prev.val:
            if curr.prev == dll.head:
                curr.prev = None
                dll.head = curr
            else:
                curr.prev.prev.next = curr
                curr.prev = curr.prev.prev
        curr = curr.next

remove_duplicate(dll)
print()
dll.traverse()