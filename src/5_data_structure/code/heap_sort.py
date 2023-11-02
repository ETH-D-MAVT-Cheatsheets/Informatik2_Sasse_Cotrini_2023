#a is a heap
def SortHeap(a):
    n = len(a)-1
    while n > 0:
        swap(a[0],a[n])
        SiftDown(a, 0, n-1)
        n = n - 1