import queue

class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def preOrder(self, root):
        if root != None:
            print(f"[{root.data}] ", end='')
            self.preOrder(root.left)
            self.preOrder(root.right)

    def inOrder(self, root):
        if root != None:
            print(f"[{root.data}] ", end='')
            self.inOrder(root.left)
            self.inOrder(root.right)

    def postOrder(self, root):
        if root != None:
            print(f"[{root.data}] ", end='')
            self.postOrder(root.left)
            self.postOrder(root.right)

    def levelOrder(self, root):
        Q = queue.Queue()
        Q.put(root)

        while not Q.empty():
            root = Q.get()
            print(f"[{root.data}] ", end='')

            if root.left != None:
                Q.put(root.left)

            if root.right != None:
                Q.put(root.right)

    def nodeCount(self, root):
        if root == None:
            return 0
        else:
            return 1 + self.nodeCount(root.left) + self.nodeCount(root.right)

    def leafNodeCount(self, root):
        if root == None:
            return 0
        else:
            if self.isExternal(root):
                return 1
            return self.nodeCount(root.left) + self.nodeCount(root.right)

    def isExternal(self, root):
        return root.left == None and root.right == None

    def getHeight(self, root):
        if root == None:
            return 0
        else:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def treeReverse(self, root):
        if root != None:
            root.left, root.right = root.right, root.left

            self.treeReverse(root.left)
            self.treeReverse(root.right)


if __name__ == '__main__':
    T = BinaryTree()

    N6 = Node('F')
    N5 = Node('E')
    N4 = Node('D')
    N3 = Node('C' , N6, None)
    N2 = Node('B', N4, N5)
    N1 = Node('A', N2, N3)

    print("Pre  : ", end=''); T.preOrder(N1); print()
    print("IN   : ", end=''); T.inOrder(N1); print()
    print("Post :", end=''); T.postOrder(N1); print()

    print("Num of Nodes : %d" % T.nodeCount(N1))
    print("Num of Leaves : %d" % T.leafNodeCount(N1))

    print("Tree Height : %d" % T.getHeight(N1))

    T.treeReverse(N1)
    print("Pre  : ", end=''); T.preOrder(N1); print()
    print("IN   : ", end=''); T.inOrder(N1); print()
    print("Post :", end=''); T.postOrder(N1); print()
    print("Level :", end=''); T.levelOrder(N1)