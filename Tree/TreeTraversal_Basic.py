class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Tree:     # Tree Class that Holds Respective Methods
    def __init__(self):
        self.root = None

    def get_pre_order_traversal(self, root):
        if root is None:
            return
        print(str(root.data)+" ", end='')
        self.get_pre_order_traversal(root.left)
        self.get_pre_order_traversal(root.right)

    def get_in_order_traversal(self, root):
        if root is None:
            return
        self.get_in_order_traversal(root.left)
        print(str(root.data)+" ", end='')
        self.get_in_order_traversal(root.right)

    def get_post_order_traversal(self, root):
        if root is None:
            return
        self.get_post_order_traversal(root.left)
        self.get_post_order_traversal(root.right)
        print(str(root.data)+" ", end='')


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

print("Pre Order")
_root.get_pre_order_traversal(_root.root)
print("\nIn Order")
_root.get_in_order_traversal(_root.root)
print("\nPost Order")
_root.get_post_order_traversal(_root.root)

