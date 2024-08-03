#count the number of vowels in a given string
def NoOfVowels(str):
    str=list(str)
    length=0
    result=[]
    for i in str:
        length+=1
    vowels=['a','e','i','o','u']
    count=0
    for x in range(0,length):
        if str[x] in vowels:
            result.append(str[x])
            count+=1
    print(count)
    print(result)
str=input();
NoOfVowels(str)