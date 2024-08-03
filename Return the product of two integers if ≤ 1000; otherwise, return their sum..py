#given two integer numbers return their product only if the product is less than or equal to 1000 or else return their sum
def product(num1,num2):
    print("Product",num1*num2)
    return num1*num2
def sum(num1,num2):
    print("Sum",num1+num2)
    return num1+num2
num1=int(input("Enter 1st number"))
num2=int(input("Enter 2nd number"))
if num1*num2<=1000:
    product(num1,num2)
else:
    sum(num1,num2)