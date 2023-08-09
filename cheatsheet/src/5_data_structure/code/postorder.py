def postorder(node):
    postorder(node.left)
    postorder(node.right)
    print(node.key)
