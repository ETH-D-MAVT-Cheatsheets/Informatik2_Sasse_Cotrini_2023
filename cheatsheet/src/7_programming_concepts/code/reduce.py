from functools import reduce
n = [1,2,3,4,5]
sum_numbers = reduce(lambda x,y: x + y, n) #15