#linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class singly_LL:
    def __init__(self):
        self.head = None
    #insert at last
    def append(self,data):
        new = Node(data)
        if self.head == None:
            self.head = new
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new
    #for traverse
    def traverse(self):
        current = self.head
        if self.head is None:
            print("empty ll")
        else:
            while current is not None:
                print("eliment is",current.data)
                current = current.next
    #insert at any position
    def insert_at(self,data,position):

        new = Node(data)
        if position == 0:
            new.next = self.head
            self.head = new
        else:
            current = self.head
            prev_Node = None
            count = 0
            while current is not None and count < position:
                prev_Node = current
                current = current.next
                count+=1
            new.next = current
            prev_Node.next = new
    #delete by value
    def delete_value(self, data):
        temp = self.head

        if self.head is None:
            print("List is empty")
            return

        # delete first node
        if temp.data == data:
            self.head = temp.next
            return

        prev = None

        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            print("value not found")
        else:
            prev.next = temp.next
                



#create linked list
sll = singly_LL()

#append nodes
sll.append(10)
sll.append(20)
sll.append(30)

print("After append:")
sll.traverse()

#insert at position
sll.insert_at(15,1)

print("After insert at position 1:")
sll.traverse()

#insert at head
sll.insert_at(5,0)

print("After insert at head:")
sll.traverse()

#delete value
sll.delete_value(20)

print("After deleting value 20:")
sll.traverse()