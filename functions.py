on = True

def add():
    a=float(input("Enter a number "))
    b=float(input("Enter another number "))
    print(a+b)

def subtraction():
    a=float(input("Enter a number "))
    b=float(input("Enter another number "))
    print(a-b)

def multiply():
    a=float(input("Enter a number "))
    b=float(input("Enter another number "))
    print(a*b)

def divide():
    a=float(input("Enter a number "))
    b=float(input("Enter another number "))
    print(a/b)

def user_info(name, age=30, city="Novo Hamburgo"):
    '''This function prints name, age and city
    from an argument provided to the function'''
    print("{} is {} years old, from {}".format(name, age, city))

"""
user_info("Karina",29, "Porto Alegre")
user_info(name="Karina",age=29)
user_info(name="Karina",city="Porto Alegre")
"""
while on:
    operation = input("Please choose +, -, *, / or q ")
    if operation == '+':
        add()
    elif operation == '-':
        subtraction()
    elif operation == '*':
        multiply()
    elif operation == '/':
        divide()
    elif operation == 'q':
        on = False
    else:
        print("This is not a valid option.")