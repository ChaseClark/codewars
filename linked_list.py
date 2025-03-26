class Node:
    def __init__(self, key):
        self.next = None
        self.data = key


class LinkedList:

    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def reverseUtil(self, curr, prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return

        next = curr.next
        curr.next = prev
        self.reverseUtil(next, curr)

    def reverse2(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print("Given Linked List")
llist.printList()

llist.reverse()
print("\nReversed Linked List")
llist.printList()
llist.reverse2()
print("\nBack to original")
llist.printList()
