def inorder(node):
    inorder(node.left)
    print(node.key)
    inorder(node.right)