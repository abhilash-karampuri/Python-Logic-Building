def Palindrome(str):
    revstr=str[::-1]
    if str==revstr:
        print("palindrome")
    else:
        print("not a palindrome")
str=input()