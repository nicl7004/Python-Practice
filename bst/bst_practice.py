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

    def inOrderTraversal(self, node,array):
        if node is not None:
            #left subtree first, then the node data, then right subtree
            self.inOrderTraversal(node.left,array)
            array.append(node.data)
            self.inOrderTraversal(node.right,array)
        return array

    def preOrderTraversal(self,node,array):
        if node is not None:
            array.append(node.data)
            self.preOrderTraversal(node.left,array)
            self.preOrderTraversal(node.right,array)
        return array

    def postOrderTraversal(self,node,array):
        if node is not None:
            self.postOrderTraversal(node.left,array)
            self.postOrderTraversal(node.right,array)
            array.append(node.data)
        return array

    def maxPathSum(self,node):
        if node.left is None and node.right is None:
            return node.data
        elif node.left is None:
            return (self.maxPathSum(node.right) + node.data)
        elif node.right is None:
            return(self.maxPathSum(node.left) + node.data)
        else:
            return(max((self.maxPathSum(node.left)+node.data), (self.maxPathSum(node.right)+node.data)))
class Sorts:
    # def __init__:
    def bubbleSort(self,array):
        for firstInd in range(len(array)):
            for secondInd in range(0,len(array)-firstInd-1):
                if array[secondInd] > array[secondInd+1]:
                    array[secondInd], array[secondInd+1] = array[secondInd+1], array[secondInd]
        return array
    def quickSort(self,array):
        pass
    def mergeSort(self,array):
        pass


def main():
    root = Node(10)
    root.left = Node(2)
    root.right   = Node(10);
    root.left.left  = Node(20);
    root.left.right = Node(1);
    root.right.right = Node(-25);
    root.right.right.left   = Node(3);
    root.right.right.right  = Node(4);
    operation = Operations()
    sorts = Sorts()
    array = [12,10,5,13,77,100,2]
    print("Tree depth is: %d" % operation.minDepth(root))
    print("Inorder traversal:", operation.inOrderTraversal(root,[]))
    print("Preorder traversal:", operation.preOrderTraversal(root,[]))
    print("Postorder traversal:", operation.postOrderTraversal(root,[]))
    print("Max path sum:", operation.maxPathSum(root))
    print("Bubblesort:", sorts.bubbleSort(array))

if __name__ == '__main__':
    main()
