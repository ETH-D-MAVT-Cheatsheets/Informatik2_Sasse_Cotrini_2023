enumerate(iterable, start) 
#iterable = iterable container (sequence)
#start (optional) = (optional) enumerate starts counting #at this number, starts at 0 when omitting start-> 
#enumerate(iterable)
#the enumerate(iterable, start) function returns a #tuple: (index, object).

for index, value in enumerate(l):
  print(index, value)
#output:
# 0 1
# 1 3
# 2 Hi
# 3 -4