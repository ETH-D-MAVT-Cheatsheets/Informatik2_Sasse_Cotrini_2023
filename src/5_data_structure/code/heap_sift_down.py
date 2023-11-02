#i is the index of the element that needs to be sifted down. a is the array. m is the end of the array
def SiftDown(a, i, m):
    while 2*i + 1 < m:
        j = 2*i + 1
        if j + 1 < m and a[j] < a[j + 1]:
            j = j + 1
        if a[i] >= a[j]:
            break
        a[i], a[j] = a[j], a[i]
        i = j
