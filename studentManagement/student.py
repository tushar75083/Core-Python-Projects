# practicing concept of dictionary

stu_data={}

def addStudent(name,grade):
    stu_data[name] = grade
    print(f"{name} is added successfully...")
    return True

def updateStudent(name):
    newGrade=input(f"Enter new grade of {name} (A/B/C/D/F) : ")
    stu_data[name]=newGrade
    print(f"{name} get updated successfully....")
    return True


def deleteStudent(name):
    del stu_data[name]
    # removedGrade=stu_data.pop(name)
    print(f"{name} get deleted successfully.....")

while True:
    print("*** Welcome To Student Mamagement System ***")
    print("...Here we manage student's name and grade... ")

    print("1.Add Student")
    print("2.Update Student")
    print("3.Delete Student")
    print("4.View Students")
    print("5.Exit")

    choice=int(input("Choose any following option : "))

    if choice==1:
        name=input("Enter name of student : ")
        grade=input(f"Enter grade of {name} (A/B/C/D/F) : ")
        keyList=stu_data.keys()
        if name not in keyList:
            addStudent(name,grade)
        else:
            print(f"{name} is already present in the list of student ...")

    elif choice==2:
        name=input("enter name which you want to update : ")
        keyList = stu_data.keys()
        if name in keyList:
            updateStudent(name)
        else:
            print(f"{name} not available in list...please try again...")

    elif choice==3:
        name=input("enter student name you want to delele : ")
        keyList=stu_data.keys()
        if name in keyList:
            deleteStudent(name)
        else:
            print(f"{name} not present in list...")
        
    
    elif choice==4:
        print(stu_data)

    elif choice==5:
        print("Thank you for using our service...")
        print("See you soon....")
        print("Program is closing....")
        break

    else:
        print("Invalid choice...Please enter valid choice...")
