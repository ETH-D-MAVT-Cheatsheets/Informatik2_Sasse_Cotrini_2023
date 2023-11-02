def heapify(a):
    n = len(a)
    for i in range(n//2 - 1, -1, -1):
        SiftDown(a, i, n)