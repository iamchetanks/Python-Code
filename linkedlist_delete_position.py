#Given a singly linked list and a position, delete a linked list node at the given position.

class LinkedList:
    def __init__(self):
        self.head = None

    def print_tree(self):
        temp = self.head
        while(temp):
            print(temp.data, end = " ")
            temp = temp.next

    def delete_node(self, x):
        count = 0
        temp = self.head
        if x == 0:
            self.head = temp.next
            return
        while(count != x-1):
            if temp.next == None:
                print("Node not found")
                return
            temp = temp.next
            count += 1
        temp.next = temp.next.next
        return



class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


def main():
    llist = LinkedList()
    llist.head = Node(1)

    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    llist.head.next = second
    second.next = third
    third.next = fourth

    llist.print_tree()
    print("\n")
    position = 3
    llist.delete_node(position)
    llist.print_tree()

if __name__ == "__main__":
    main()