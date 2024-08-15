def task():
    tasks=[]
    print("*** Welcome To Task Management System ***")

    num=int(input("How many tasks you want to add ?"))

    for n in range(1,num+1):
        task=input(f"enter your task {n} : ")
        tasks.append(task)

    print("All Tasks are :")
    print(tasks)

    while True:
        print("1. Add task")
        print("2. Update task")
        print("3. Delete task")
        print("4. View task")
        print("5. Exit")

        choice=int(input("Please enter your choice(in digit) : "))
        if choice==1:
            task=input("enter your task : ")
            if task not in tasks:
                tasks.append(task)
                print(f"{task} has been successfully added in list")
            else:
                print(f"{task} is present in list..add something different task..")
        elif choice==2:
            task1=input("enter task name which you want to update : ")
            if task1 in tasks:
                new_task=input("enter new task to add : ")
                ind=tasks.index(task1)
                tasks[ind]=new_task
                print(f"list get updated successfully..{new_task} added in the list")
            else:
                print(f"{task1} is not present inside the list...")
                print("Please enter task which is already present inside the list...")
        elif choice==3:
            task=input("Enter task which you want to delete : ")
            if task in tasks:
                ind=tasks.index(task)
                del tasks[ind]
                print(f"{task} has been deleted successfully...")
            else:
                print(f"{task} is not present in tasks list...")
        elif choice==4:
            print("All tasks are as follows : ")
            print(tasks)
        elif choice==5:
            print("Program is closing ...See you soon...")
            break
        else:
            print("Invalid choice...")


task()





