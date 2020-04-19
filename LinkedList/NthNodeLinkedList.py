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

    def nth_node_from_last(self, key):
        head = self.head
        slow_pointer = head
        fast_pointer = head
        counter = 0
        while fast_pointer is not None:
            if counter > key:
                slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
            counter += 1

        print("Node from Last "+str(key)+" is "+str(slow_pointer.data))
        return slow_pointer


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

_list.nth_node_from_last(3)
