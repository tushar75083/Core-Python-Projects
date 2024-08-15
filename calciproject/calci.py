# this is a menu driven program which can perform some basic arithmetic operations on user entered values

print("***   Welcome To Our Project  ***")
print("*** Make any calculation easily  ***")

while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

    choice=int(input('Choose any option(digit): '))
    num1=int(input("enter first number : "))
    num2=int(input("enter second number : "))

    if choice == 1:
        result = num1+num2
        print(f"Addition of {num1} and {num2} is {result}")
    elif choice == 2:
        result = num1-num2
        print(f"Subtraction of {num1} and {num2} is {result}")

    elif choice == 3:
        result = num1*num2
        print(f"Multiplicatiion of {num1} and {num2} is {result}")

    elif choice == 4:
        result = num1/num2
        result=round(result,2)
        print(f"division of {num1} and {num2} is {result}")

    else:
        print("Invalid Choice..")

    ans=input("You want to continue ? (y/n)")
    ans=ans.lower()
    if ans!='y':
        break

    
