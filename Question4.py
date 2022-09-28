# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.) 					[2]

def myprog():
    a=input("Enter a word to check ")
    a=a.casefold()
    b=reversed(a)
    if list(a) == list(b):
        print(f"{a} is a Palindrome.")
    else:
        print(f"{a} is not a Palindrome.")
myprog()