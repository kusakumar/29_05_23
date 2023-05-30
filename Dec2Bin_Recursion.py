## Decimal to binary with recurion method
def dectobin(n):
    r=n%2
    if(n!=0):  #if n>=1:
        dectobin(n//2)
        print(r,end=' ')
n=int(input("Enter the value: "))
dectobin(n)
print()
