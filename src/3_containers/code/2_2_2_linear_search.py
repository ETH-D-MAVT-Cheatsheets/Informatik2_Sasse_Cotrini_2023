#Input: array a, key b
#Output: index k with a[k] = b or "not found"
def LinearSearch(a, b):
    for i, x in enumerate(a):
        if x == b:
            return i
        return "not found"