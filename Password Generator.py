#password generator
import random
import string
'''capital words
small leters
numbers
symbols'''
Symbols=['@','#','$']
alphabets=list(string.ascii_letters)
numbers=[]
for i in range(0,10):
    Symbols.append(i)
password=Symbols+alphabets
for j in range(8):
    value=random.choice(password)
    print(value, end="")