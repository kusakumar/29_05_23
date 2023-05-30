#Method:1 reverse the string with help of loop.

def reverse(string):
    str=""
    for i in string:
        str=i+str #string togther,Use the + character to add a variable to another variable
    return str
string = input("Enter the string: ")
print("Original string is: ",string)
print("Reverse string is :",reverse(string))
print()

# Method2: Reverse the string by using recursion
"""In the function, the base condition is that if the length of the string is equal to 0, the string is returned. 
If not equal to 0, the reverse function is recursively called to slice the part of the string except the first character 
and concatenate the first character to the end of the sliced string"""

#finding string length or by using len function
string=input("Enter the string name:")
length=0
for i in string:
    length+=1
print(length)
print()
print(string[::-1])
#reverse the string by using string slicing
def reverse(string):
    # Complete this recursive function
    if len(string)==0:
        return string
    else:
        return reverse(string[1:])+string[0]
string = input("Enter the string: ")
print("Original string is: ",string)
print("Reverse string is :",reverse(string))
print()

###Method3: Reverse the string with using an extended slice

def reverse(string):
    string = string[::-1]
    return string
string = input("Enter the string: ")
print("Original string is: ",string)
print("Reverse string is :",reverse(string))
print()