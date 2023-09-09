tasks = []


def add_task(task):
    tasks.append(task)


def remove_task(i):
    tasks.pop(i)


def list_tasks():
    for item in tasks:
        print(item)


def export_tasks():
    with open("tasks.txt", "w") as file:
        i = 0
        while i < len(tasks):
            file.write(str(i + 1) + ". " + tasks[i] + "\n")
            i += 1


print("Welcome to Basic TODOs App with Python!")

while True:
    print("---------------------------------------------")
    print("Options:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Export Tasks to txt file")
    print("5. Quit")

    user_input = input("Choose an option: ")

    if user_input == "1":
        t = input("Add task: ")
        add_task(t)
    elif user_input == "2":
        i = input("Which task do you want to delete? (Ex. input: 1): ")
        if i.isdigit():
            if int(i) <= len(tasks):
                remove_task(int(i) - 1)
                print("Task " + i + " successfully removed.")
            else:
                print("There is no task with number " + i + "!")
        else:
            print("Invalid input.")
    elif user_input == "3":
        print("---------------------------------------------")
        print("Tasks:")
        i = 0
        while i < len(tasks):
            print(str(i + 1) + ". " + tasks[i])
            i += 1
    elif user_input == "4":
        export_tasks()
    elif user_input == "5":
        break
    else:
        print("Invalid option!")
