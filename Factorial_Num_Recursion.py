###factiorial of given numbers

def fact(n):
     if n==1:
        return 1
     else: return n*fact(n-1)
n=int(input("Enter the value: "))
res=fact(n)
print(res)
print()

# without recursion function
print("Without Recusion, Factorial of N: ")
print()
n=int(input("Enter the value: "))
r=1
for i in range(1,n+1):
    r*=i
print("Factional of N is :",r)



