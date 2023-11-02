def merge(a1, a2):
    b, i, j = [], 0, 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            b.append(a1[i])
            i += 1
        else:
            b.append(a2[j])
            j += 1
    b += a1[i:]
    b += a2[j:]
    return b

def merge_sort(a):
    if len(a) <= 1:
        return a
    else:
        sorted_a1 = merge_sort(a[:len(a) // 2])
        sorted_a2 = merge_sort(a[len(a) // 2:])
        return merge(sorted_a1, sorted_a2)
