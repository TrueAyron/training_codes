class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def remove(self, data):
        # helper function to find the node to be removed and its parent
        def find_node_and_parent(node, data, parent=None):
            if node is None:
                return None, None
            if node.data == data:
                return node, parent
            if data < node.data:
                return find_node_and_parent(node.left, data, node)
            else:
                return find_node_and_parent(node.right, data, node)

        # remove the node
        node, parent = find_node_and_parent(self.root, data)
        if node is None:
            return  # data not found
        if node.left is None and node.right is None:  # leaf node
            if parent is None:  # root node
                self.root = None
            elif parent.left == node:
                parent.left = None
            else:
                parent.right = None
        elif node.left is None or node.right is None:  # one child
            if parent is None:  # root node
                self.root = node.left if node.left is not None else node.right
            elif parent.left == node:
                parent.left = node.left if node.left is not None else node.right
            else:
                parent.right = node.left if node.left is not None else node.right
        else:  # two children
            # find the in-order predecessor
            current = node.left
            parent = None
            while current.right is not None:
                parent = current
                current = current.right
            node.data = current.data  # copy the data from the in-order predecessor
            if parent is None:  # the in-order predecessor is the left child of the node
                node.left = current.left
            else:  # the in-order predecessor is somewhere in the left subtree
                parent.right = current.left
