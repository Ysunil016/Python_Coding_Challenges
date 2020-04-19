class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class SingleLinkedList:  # Single Linked List Implementation
    def __init__(self):
        self.head = None

    def print_element_in_linked_list(self, key):
        head = self.head
        while head is not None:
            if head.data == key:
                return True
            head = head.next
        return False

    def display_elements_in_linked_list(self):
        head = self.head
        while head is not None:
            print(head.data+" "),  # Printing InLine
            head = head.next


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

# Printing all the Elements in the Linked List
print("Element Found "+str(_list.print_element_in_linked_list("Four")))
print("Displaying All the Elements in SingleLinkedList")
_list.display_elements_in_linked_list()

