#Input: sorted array a, key b
#Output : index k with a [ k ] = b or " not found "
def bin_search(a, l, r, b):
    if r < l:
        return None
    else:
        m = (l + r) // 2
        if a[m] == b:
            return m
        elif b < a[m]:
            return bin_search(a, l, m-1, b)
        else: # a[m] > b
            return bin_search(a, m+1, r, b)
