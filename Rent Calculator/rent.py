print("*** Welcome To Our Rent Calculator Project ***")
print("Now Calculate Individual Rent Easily.....")

print("Please enter below Details : ")
persons=int(input("Enter number of persons living in room : "))
room_rent=int(input("enter total room rent : "))
elec_bill=int(input("enter electricity bill : "))
water_bill=int(input("enter water bill : "))
meal =int(input("enter the meal expense : "))
other=int(input("enter other expenses :"))

total_expense = room_rent + elec_bill + water_bill + meal + other
ind_expense=total_expense / persons
ind_expense=round(ind_expense,2)
print(f"Individual rent is Rs.{ind_expense}")