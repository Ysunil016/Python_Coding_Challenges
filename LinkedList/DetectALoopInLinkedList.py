class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def has_loop(self):
        head = self.head
        slow_pointer = head
        fast_pointer = head
        while fast_pointer.next is not None and fast_pointer is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False


_nodeA = Node("One")
_nodeB = Node("Two")
_nodeC = Node("Three")
_nodeD = Node("Four")
_nodeE = Node("Five")

_list = LinkedList()
_list.head = _nodeA
_nodeA.next = _nodeB
_nodeB.next = _nodeC
_nodeC.next = _nodeD
_nodeD.next = _nodeE
_nodeE.next = _nodeC

print(_list.has_loop())

