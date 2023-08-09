def SiftUp(a, m):
    v = a[m]
    c = m
    p = c//2
    while c > 0 and v > a[p]:
        a[c] = a[p]
        c = p
        p = c//2
    a[c] = v
