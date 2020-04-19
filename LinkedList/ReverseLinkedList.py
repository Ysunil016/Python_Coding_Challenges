class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class SingleLinkedList:  # Single Linked List Implementation
    def __init__(self):
        self.head = None

    def display_linked_list(self):
        head = self.head
        while head is not None:
            print(str(head.data)+" ", end='')
            head = head.next

    def reverse_linked_list(self):
        head = self.head
        prev = None
        while head is not None:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        self.head = prev


_nodeA = Node("One")
_nodeB = Node("Two")
_nodeC = Node("Three")
_nodeD = Node("Four")
_nodeE = Node("Five")

_list = SingleLinkedList()
_list.head = _nodeA
_nodeA.next = _nodeB
_nodeB.next = _nodeC
_nodeC.next = _nodeD
_nodeD.next = _nodeE

_list.reverse_linked_list()
_list.display_linked_list()

