def findSuccessor(start_node):
    parent = None  
    node = start_node.right
    while node.left is not None:
        parent = node
        node = node.left
    return node

def deleteNode(root, key):
    if root is None:
        return None
    # Find the node to be deleted
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # Case 1: Node has no children
        if root.left is None and root.right is \
            None:
            root = None
        # Case 2: Node has one child
        elif root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
        # Case 3: Node has two children
        else:
            successor = findSuccessor(root)
            root.val = successor.val
            root.right = deleteNode(root.right,\
               successor.val)
    return root
