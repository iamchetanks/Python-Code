class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    def printllist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)


llist.head.next = second
second.next = third

print("print list")
llist.printllist()
