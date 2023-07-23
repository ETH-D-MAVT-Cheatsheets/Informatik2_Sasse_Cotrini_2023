#Input: Array a = (a[0],...,a[n]) 
#Output: Sorted Array a
def sort(a):
    n = len(a)
    for i in range(n):
        mini = i
        for j in range(i+1, n):
            if a[j] < a[mini]:
                mini = j
        a[mini],a[i] = a[i],a[mini]
    return a