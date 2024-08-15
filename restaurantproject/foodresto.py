print("***  Welcome To Our Restaurant  ***")
print("***  Serving Best Quality Food  ***")

menu={
    'Burger': 150,
    'Pasta' : 70,
    'Pizza' : 120,
    'Salad' : 80,
    'Coffee' :60,
}
total_bill=0
while True:
    print("Menu List :")
    print("1.Burger   ==>  Rs.150")
    print("2.Pasta    ==>  Rs.70")
    print("3.Pizza    ==>  Rs.120")
    print("4.Salad    ==>  Rs.80")
    print("5.Coffee   ==>  Rs.60") 

    choice = input("Please make your order : ")
    
    if choice=='Burger' or choice == '1':
        total_bill+=menu["Burger"]
        print(f"Your order of Burger is accepted..")
    elif choice=='Pasta' or choice =='2':
        total_bill+=menu["Pasta"]
        print(f"Your order of Pasta is accepted..")
    elif choice=='Pizza' or choice == '3':
        total_bill+=menu["Pizza"]
        print(f"Your order of Pizza is accepted..")
    elif choice=='Salad' or choice == '4':
        total_bill+=menu["Salad"]
        print(f"Your order of Salad is accepted..")
    elif choice=='Coffee' or choice =='5':
        total_bill+=menu["Coffee"]
        print(f"Your order of Coffee is accepted..")
    else:
        print("Sorry...This food item is not available...")
    
    ans=input("Is there any other order ? (y/n)")
    ans=ans.lower()
    if ans != 'y':
        break

print(f"Your total bill amount is Rs.{total_bill}")
print("Thank you for visiting our Restaurant...")
print("Have a good Day...See you soon...")