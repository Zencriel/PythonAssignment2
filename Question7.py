# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers,
# and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your code in a method.

import random
def myprog():
    a = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    b = 8
    c = "".join(random.sample(a,b ))
    print(f"Your randomly generated password is {c}")
myprog()
