def insert(heap, value):
    heap.append(value)
    SiftUp(heap, len(heap)-1)
