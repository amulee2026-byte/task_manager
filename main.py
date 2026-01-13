tasks = []

def show_menu():
    print("\n Task Manager")
    print("1. Add task")
    print("2. View task")
    print("3. Exit")

def add_task():
    task = input("Enter task:")
    tasks.append(task)
    print("Task added!")

def main():
    while True:
        show_menu()
        choice = input("choose an option:")

        if choice == "1":
            add_task()
        elif choice == "2":
            print(tasks)
        elif choice =="3":
            print("Goodbye !")
            break
        else:
            print("Invalid choice")

        
main()

