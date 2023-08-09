def print_elements(l):
    current = l.head
    while current != None:
        print(current.value)
        current = current.Next
