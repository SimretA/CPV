from adder import add
from mult import multiply
from sub import sub

if __name__ == '__main__':
    choice = eval(input("Enter 1. to add\n2. to sub\n3. to multiply.\n4. to divide"))
    num1 = input("Enter first number")
    num2 = input("Enter second number")
    if choice == 1:
        add(num1, num2)
    elif choice == 2:
        sub(num1, num2)
    elif choice == 3:
        multiply(num1, num2)
    elif choice == 4:
        div(num1, num2)

