class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display_linked_list(self):
        head = self.head
        while head is not None:
            print(str(head.data)+" ", end='')
            head = head.next

    def remove_node_from_linked_list(self, key):
        head = self.head
        prev = None
        while head is not None:
            if head.data == key:
                if prev is not None:
                    prev.next = head.next
                else:
                    self.head = head.next
            prev = head
            head = head.next


_nodeA = Node("One")
_nodeB = Node("Two")
_nodeC = Node("One")
_nodeD = Node("Four")
_nodeE = Node("One")

_list = LinkedList()
_list.head = _nodeA
_nodeA.next = _nodeB
_nodeB.next = _nodeC
_nodeC.next = _nodeD
_nodeD.next = _nodeE

_list.display_linked_list()
_list.remove_node_from_linked_list("One")
print()
_list.display_linked_list()
