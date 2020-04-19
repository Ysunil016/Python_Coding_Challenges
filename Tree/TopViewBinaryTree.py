from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def view(self):
        root = self.root

        class FareObj:
            def __init__(self, node, height):
                self.node = node
                self.height = height
        queue = deque()
        queue.append(FareObj(root, 0))

        view_set = {}

        while True:
            queue_count = len(queue)
            if queue_count == 0:
                break

            while queue_count > 0:
                current_node = queue.popleft()
                if current_node.node.left is not None:
                    queue.append(FareObj(current_node.node.left, current_node.height-1))
                if current_node.node.right is not None:
                    queue.append(FareObj(current_node.node.right, current_node.height+1))
                queue_count -= 1
                if view_set.get(current_node.height) is None:
                    view_set[current_node.height] = current_node.node.data
        for x in sorted(view_set.keys()):
            print(str(view_set.get(x))+" ", end='')


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

_root.view()
