def insert_after_node(node, value):
    new_node = Node(value, node.Next)
    node.Next = new_node

def insert_after_value(l, value, new_value):
    node = search(l, value)
    if node != None:
        insert_after_node(node, new_value)
