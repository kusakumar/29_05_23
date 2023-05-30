####Method:1

# Recursive function to return gcd of a and b
def gcd(a, b):
    # Everything divides 0
    if (a == 0):
        return b
    if (b == 0):
        return a
    # base case
    if (a == b):
        return a
    # a is greater
    if (a > b):
        return gcd(a - b, b)
    return gcd(a, b - a)


# Driver program to test above function
a = int(input("Enter first value: "))
b = int(input("Enter first value: "))
if (gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
    print('not found')

print()

####Method:2

def GCD(a, b):
    if (b == 0):
        return a
    else:
        return GCD(b, a % b)


a = int(input("Enter first value: "))
b = int(input("Enter first value: "))

# prints 12
print("The gcd of a and b is : ", end="")
print(GCD(a, b))
print()

####Method:3
num1 = int(input("Enter first value: "))
num2 = int(input("Enter first value: "))
while num1 != num2:
    if num1 > num2:
        num1 -= num2
    else:
        num2 -= num1

print("GCD of num1 and num2 is", num1)