#Count number of alphabets and number of digits in a sentence
def Sentence(sent):
    list=[]
    alist=[]
    numlist=[]
    for x in n:
        list.append(x)
    for y in list:
        if y.isdigit():
          numlist.append(y)
        else:
            alist.append(y)
    numlist=set(numlist)
    alist=set(alist)
    alist.remove(' ')
    print("number of alphabets in the given sentence: ",len(alist))
    print("number of digits are:",len(numlist))
n=input("enter a sentence:")
Sentence(n)
