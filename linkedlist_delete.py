#Given a ‘key’, delete the first occurrence of this key in linked list.

class Linkedlist:
    def __init__(self):
        self.head = None

    def printtree(self):
        temp = self.head
        while(temp):
            print(temp.data, end = " ")
            temp = temp.next

    def deletenode(self, key):
        if key == self.head.data:
            self.head = self.head.next
            return

        temp = self.head
        while(temp.next.data != key):
            temp = temp.next
            if temp.next == None:
                print("No key found")
                return
        temp.next = temp.next.next


class Node:
    def __init__(self, key):
        self.data = key
        self.next = None

def main():
    llist = Linkedlist()
    llist.head = Node(10)

    second = Node(20)
    third = Node(30)
    fourth = Node(40)

    llist.head.next = second
    second.next = third
    third.next = fourth

    llist.printtree()
    print("\n")

    llist.deletenode(50)
    llist.printtree()
    print("\n")

    llist.deletenode(30)
    llist.printtree()
    print("\n")


if __name__ == "__main__":
    main()
