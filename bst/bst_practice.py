# BST data structure and different operations preformed on it

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Operations:
    # def __init__(self):
    def minDepth(self, node):
        # for edge case of null root
        if node is None:
            return 0
        # for base case of having 2 leafs
        elif node.left == None and node.right == None:
            return 1
        elif node.left == None:
            return self.minDepth(node.left)+1
        elif node.right == None:
            return self.minDepth(node.right)+1

        else:
            return min(self.minDepth(node.left), self.minDepth(node.right))+1

    def inOrderTraversal(self, node):
        if node is not None:
            #left subtree first, then the node data, then right subtree
            self.inOrderTraversal(node.left)
            print(node.data)
            self.inOrderTraversal(node.right)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    operation = Operations()
    print("Tree depth is: %d" % operation.minDepth(root))
    operation.inOrderTraversal(root)

if __name__ == '__main__':
    main()
