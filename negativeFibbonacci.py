"""Mission:
Let's define a new Fibonacci series called "Negative Fibonacci" as follow: 
index: ... -4 -3 -2 - 1 0 1 2 3 4 ... 
value: ... -3 2 -1 1 0 1 1 2 3 ... 
The value of tem at position i equals to the addition of the two previous values. 
For example: fib(-1) = fib(-3) + fib(-2)
(a) Please write a "fib" function that got an index and returns its value e.g. 
	for fib(3) returns 2 and for fib(-4) returns -3
"""

"""
Some Math:
for n>0: 
fib(n) = fib(n-1)+fib(n-2) 
for n<0: 
fib(n) = fib(n-1)+fib(n-2) 
fib(n-2) = fib(n)-fib(n-1) 
i = n-2 ==> n=i+2 fib(i) = fib(i+2)-fib(i+1)
"""

# a recursive function to find the value, using the math calculation specified above

def fib_a(n):
    
    if n==0:
        return 0
    if n==1 or n==-1:
        return 1
    if n>1:
        return fib_a(n-1)+fib_a(n-2)
    if n<-1:
        return fib_a(n+2)-fib_a(n+1)

"""
(b) Assuming you have additional memory. Please implement an improved function to get better performance.
"""

# This time will use the additional memory to avoid calculating value of same index more then once.
import numpy as np

def fib_b(n):
    
    # define the additional memory
    series = np.zeros(abs(n)+1)
    #call a new recursive function, with the extra memory
    return fibbo(n,series)


def fibbo(n,series):
    
    if n==0:
        return 0
    if n==1 or n==-1:
        return 1
    if n>1:
    	# if the value of this index not yet calculated, call the function to make the calculation
        if series[n]==0:
            series[n] = fibbo(n-1,series) + fibbo(n-2,series)
    if n<-1:
        if series[n]==0:
            series[n] = fibbo(n+2,series) - fibbo(n+1,series)
    return series[n]

def main():

	while True:
		try:
			index = int(input("Please choose an index: "))
		except:
			print ("not an integer")
			continue
		else:
			res_a = fib_a(index)
			res_b = fib_b(index)
			break

	print("Result of first function: ", res_a)
	print("Result of second function: ", res_b)


if __name__ == '__main__':
    main()
