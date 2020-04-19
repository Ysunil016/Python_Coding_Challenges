class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class SingleLinkedList:  # Single Linked List Implementation
    def __init__(self):
        self.head = None

    def middle_node(self):
        head = self.head
        slow = head
        fast = head
        while fast is not None and fast.next is not None :
            slow = slow.next
            fast = fast.next.next
        return slow


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

print(_list.middle_node().data)

