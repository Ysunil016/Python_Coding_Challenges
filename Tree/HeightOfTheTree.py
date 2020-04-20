
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None


def height_of_the_tree(root):
    if root is None:
        return 0
    return max(height_of_the_tree(root.left), height_of_the_tree(root.right)) + 1


_node_10 = Node(10)
_node_20 = Node(20)
_node_30 = Node(30)
_node_40 = Node(40)
_node_50 = Node(50)
_node_60 = Node(60)
_node_70 = Node(70)
_node_80 = Node(80)
_node_90 = Node(90)

_root = Tree()
_root.root = _node_10
_node_10.left = _node_20
_node_10.right = _node_30
_node_20.left = _node_40
_node_20.right = _node_50
_node_30.left = _node_60
_node_30.right = _node_70
_node_40.left = _node_80
_node_40.right = _node_90

print(height_of_the_tree(_root.root))
