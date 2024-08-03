#calculator Program to perform arithmetic operations on two numbers
n1=int(input())
op=input("Enter Operator:")
n2=int(input())
def match_case(op):
    match op:
        case '+':
            return n1+n2
        case '-':
            return n1-n2
        case '*':
            return n1*n2
        case '/':
            return n1/n2
result=match_case(op)
print(result)
    