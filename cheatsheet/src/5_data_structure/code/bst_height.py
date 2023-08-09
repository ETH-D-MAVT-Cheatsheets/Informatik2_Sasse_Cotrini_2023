def height(node):
    if node == None:
        return 0
    else:
        return 1 + max(height(node.left), height(node.right))
