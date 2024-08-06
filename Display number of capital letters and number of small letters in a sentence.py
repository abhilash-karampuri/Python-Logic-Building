#Display number of capital letters and number of small letters in a sentence
n=input()
list=[]
upper =0
lower=0
for x in n:
    list.append(x)
for y in list:
    if y.isupper():
        upper+=1
    elif y.islower():
        lower+=1
print(upper)
print(lower)
