def preorder(node):
    print(node.key)
    preorder(node.left)
    preorder(node.right)