F = [None] * (n+1)
#border cases
F[0] = 1
F[1] = 1
#Bottom-Up for loop
for i in range(2, n+1):
    F[i] = F[i-1] + F[i-2]
fib_n = F[n]