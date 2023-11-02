def removeMax(heap):
    if len(heap) == 0:
        return None
    max_val = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    SiftDown(heap, 0, len(heap)-1)
    return max_val
