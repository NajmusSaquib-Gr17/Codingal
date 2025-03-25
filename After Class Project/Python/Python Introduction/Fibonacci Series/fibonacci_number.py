#import sys

#sys.set_int_max_str_digits(10000)

n = int(input("Enter the Term, n: "))

def fibSeries(n):
    fib_series = [0, 1]
    for i in range(2, n):
        nextTerm = fib_series[-1] + fib_series[-2]
        fib_series.append(nextTerm)
    return fib_series[:n]

if n < 0:
    print("The number must be a positive integer")
else:
    print(f"Fibonacci Series Upto {n}th term ==>")
    print (fibSeries(n))