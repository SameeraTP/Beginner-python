calculator='''
_____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
print(calculator)
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def div(n1,n2):
    return n1/n2
def mul(n1,n2):
    return n1*n2
operations={"+":add,
            "-":sub,
            "/":div,
            "*":mul}
def calculations():
    num1=float(input("what is the 1st number?:\n"))
    should_continue=True
    while should_continue:
        for i in operations:
            print(i)
        operation_symbol=input("pick one operation:\n")
        num2=float(input("what is the 2nd number?:\n"))
        result=operations[operation_symbol](num1,num2)
        print(f"{num1}{operation_symbol}{num2}={result}")
        choice=input("Type y for continue otherwise type n , type end for exit:\n").lower()
        if choice=="y":
            num1=result
        elif choice=="end":
            exit()
        else:
            should_continue=False
            print("\n"*20)
            calculations()
calculations()
