def remove_after_node(node):
    to_remove = node.Next
    if to_remove == None:
        return
    else:
        node.Next = to_remove.Next

def remove_after_value(l, value):
    node = search(l, value)
    if node != None:
        remove_after_node(node)
