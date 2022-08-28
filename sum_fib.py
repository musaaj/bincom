fib = [0, 1]

for i in range(48):
    fib.append(fib[len(fib) - 1] + fib[len(fib)-2])

print("sum of the first fifty fibonacci numbers is {0}".format( sum (fib)))
