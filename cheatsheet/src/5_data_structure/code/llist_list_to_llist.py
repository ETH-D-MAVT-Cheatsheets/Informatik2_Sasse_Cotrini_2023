"""Create and return linked list from list a."""
def create_from_list(a):
    l = Linked_List(Node(a[0]))
    last = l.head
    for v in a[1:]:
        last.Next = Node(v)
        last = last.Next
    return l
