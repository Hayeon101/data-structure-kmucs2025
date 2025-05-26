class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root == None:
        return TreeNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        pass

    return root

def getMinNode(root):
    while root != None and root.left != None:
        root = root.left

    return root

def delete(root, key):
    if root == None:
        return None

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            succ = getMinNode(root.right)
            root.key = succ.key
            root.right = delete(root.right, succ.key)

    return root

def preOrder(root):
    if root != None:
        print('%2d ' % root.key, end = '')
        preOrder(root.left)
        preOrder(root.right)

def display(root, msg):
    print(msg, end = '')
    preOrder(root)
    print()


if __name__ == '__main__':
    root = None
    data = [35,18,7,26,3,22,30,12,26,68,99]

    for key in data:
        root = insert(root, key)
        display(root, '[Insert %2d] : ' % key)
    print()

    # root = delete(root, 30)
    # display(root, '[Delete 30] : ')
    # root = delete(root, 26)
    # display(root,'[Delete 26] : ')

    root = delete(root, 18)
    display(root, '[Delete 18] : ')