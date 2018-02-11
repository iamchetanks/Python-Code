class Linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data, end =" ")
            temp = temp.next
        print("\n")

    def insertAtBeginning(self, value):
        beginningNode = Node(value)
        beginningNode.next = self.head
        self.head = beginningNode

    def intertAtEnd(self, value):
        endNode = Node(value)
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = endNode

    def insertAfterNode(self, prev_node, value):
        newNode = Node(value)
        newNode.next = prev_node.next
        prev_node.next = newNode



class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


def create_linked_list():
    llist = Linkedlist()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third
    return llist

def main(llist):
    print("print list")
    llist.printlist()

    llist.insertAtBeginning(10)

    print("insert at beginning")
    llist.printlist()

    print("insert at end")
    llist.intertAtEnd(20)

    llist.printlist()

    print("insert after a given node")
    llist.insertAfterNode(llist.head.next, 50)
    llist.printlist()


if __name__ == "__main__":
    llist = create_linked_list()
    main(llist)