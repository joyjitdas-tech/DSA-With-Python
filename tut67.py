#Delete All Occurrences of a Key in Doubly Linked List
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
dll.append(10)
dll.append(20)
dll.append(10)
dll.append(40)
dll.append(50)
dll.append(10)

print("After append:")
dll.traverse()

def delete_Node(dll, val):
    curr = dll.head

    while curr:
        
        nxt = curr.next
        if curr.val == val:

            if curr.prev:             # middle or tail
                curr.prev.next = curr.next
            else:                     # head node
                dll.head = curr.next

            if curr.next:             # fix backward link
                curr.next.prev = curr.prev

        curr = nxt
        

delete_Node(dll,50)
print()
dll.traverse()