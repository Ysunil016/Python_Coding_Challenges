class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


listOne = Node("One")
listOne.next = Node("Two")
listOne.next.next = Node("Three")
listOne.next.next.next = Node("Four")
listOne.next.next.next.next = Node("Five")

# Printing all the Elements in the Linked List


def search_element(_list, key):
    while _list is not None:
        if _list.data == key:
            return True
        _list = _list.next
    return False


print(search_element(listOne, "Three"))


