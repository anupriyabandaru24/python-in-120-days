def load_tasks():
    try:
        with open("tasks.txt","r") as f:
             task_list=[]
             for line in f:
                  task_list.append(line.strip())
             return task_list
    except FileNotFoundError:
        return []             
def save_tasks(tasks):
    with open("tasks.txt","w") as f:
        for line in tasks:
            f.write(line +"\n")
def add_task(tasks,task):
    tasks.append(task)
    return tasks
def view_tasks(tasks):
    if len(tasks)==0:
        print("No tasks yet")
    for index,task in enumerate(tasks):
        print(f"{index+1}. {task}")
def remove_task(tasks,index):
    try:
        tasks.pop(index)
        return tasks
    except IndexError:
        print("Index is invalid")
        return tasks 
tasks = load_tasks()
while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Save & Exit")
    try:
        option=int(input("Choose an option: "))
    except ValueError:
        print("Please enter a number")
        continue
    if option==1:
        task=input("Enter new task:")
        tasks=add_task(tasks, task)
    elif option==2:
        view_tasks(tasks)
    elif option==3:
        try:
           index=int(input("Enter task number to remove:"))
        except ValueError:
            print("Enter valid index:")
            continuwe
        tasks=remove_task(tasks,index-1)
    elif option==4:
            save_tasks(tasks)
            break
    else:
        print("Enter a number between 1 and 4")      