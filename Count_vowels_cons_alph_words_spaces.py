## Count vowels and consonants in given string

s=input("Enter the string: ")
vowel= 0
const=0
vowels=["a","e","i","o","u","A","E","I","O","U"]
for i in s:
    if i in vowels:
        vowel+=1
    else:
        const+=1
print(vowel,const)
print()

####Count words and spaces and alphebets in given string