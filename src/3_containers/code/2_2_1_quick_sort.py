def partition(a, l, r):
    p = a[r]
    j = l
    for i in range(l, r):
        if a[i] < p:
            a[i], a[j] = a[j], a[i]
            j += 1
    a[j], a[r] = a[r], a[j]
    return j

def quicksort(a, l, r):
    if l < r:
        k = partition(a, l, r)
        quicksort(a, l, k - 1)
        quicksort(a, k + 1, r)