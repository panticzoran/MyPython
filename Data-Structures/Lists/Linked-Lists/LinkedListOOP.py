# Implementation of Linked Lists using OOP

class Node:
    # Represents each element in the linked list
    # Stores data and the reference to the next node
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Class for operations with linked lists
    
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


# Testing
myLinkedList = LinkedList()
myLinkedList.append("A")
myLinkedList.append("B")
myLinkedList.append("C")
myLinkedList.print_list()  # Prints A, B and C, line by line