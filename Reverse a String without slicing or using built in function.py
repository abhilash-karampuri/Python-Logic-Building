#reverse a string without using any built in functions
def ReverseString(str):
    empty=""
    for x in str:
        empty=x+empty
    print(empty)
str=input()
ReverseString(str)