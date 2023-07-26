lambda arguments : expression
#Lambda with one argument:
n = [1,2,3,4,5]
sqrd_numbers = map(lambda x : x**2, n)
print(list(sqrd_numbers)) #[1,4,9,16,25]
#Lambda with multiple arguments:
y = lambda x,y: x*y
y(5,3) #15