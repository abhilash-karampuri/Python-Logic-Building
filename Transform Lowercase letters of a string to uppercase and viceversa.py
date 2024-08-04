#given a string combination of both upper and Lowe case letters. Transform all lower case to upper case and upper case to lower case letters in a string.
str = "AbhI"
newstr = ""

for char in str:
    if char.islower():
        newstr += char.upper()
    elif char.isupper():
        newstr += char.lower()
    else:
        newstr += char  

print(newstr)
