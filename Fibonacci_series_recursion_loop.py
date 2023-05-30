#### Using recursion
###Method:1
def fib(n):
    if n<0:
        print("Valid entry")
    elif n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter the nth fabinacci number: "))
print(fib(n))
print()

####Without recursion
###Method:1

def fib(n):
    a=0
    b=1
    if n<0:
        print("Enter valid number to generate the fibanacci series")
    elif n==0:
        return a
    elif n==1:
        return b
    else:
        print("Fibonacci Series:", a, b, end=" ")
        for i in range(1, n):
            c = a + b
            a = b
            b = c
            print(c,end=' ')
        return b
n=int(input("Enter the nth fabinacci number: "))
nth_term=fib(n)
print()
print(nth_term)
print()
print("Method:2")
###printing nth series
# check if the number of terms is valid
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))
# first two terms
n1, n2 = 0, 1
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   for i in range(1,nterms+1):
       print(n1,end=' ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       #print(nth,end=' ')


#Method:3

# Write a program to print fibonacci series upto n terms in python
num = 9
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()