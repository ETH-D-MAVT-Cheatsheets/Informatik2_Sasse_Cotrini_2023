def search(l, v):
    current = l.head
    while current != None:
        if current.value == v:
            return current
        current = current.Next
    return None