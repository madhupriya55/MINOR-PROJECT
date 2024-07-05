tasks=[]
def addTask():
    task=input("enter a task: ")
    tasks.append(task)
    
def delTask():
    listTasks()
    try:
        tasktodelete=int(input("enter a task to delete: 0"))
        if tasktodelete>=0 and tasktodelete<len(tasks):
            tasks.pop(tasktodelete)
            print(f"task '{tasktodelete}' has removed.")
        else:
            print(f"task '{tasktodelete}' has not found.")
    except:
        print("invalid input")
def listTasks():
    if not tasks:
        print("there are no tasks currently")
    else:
        for index,task in enumerate(tasks):
            print(f"Task #{index}. {task}")
        
        
if __name__ =="__main__":
    print("welcome to to do list app : ")
    while True:
        print("please select one of the following options: ")
        print("-------------------------------------------")
        print("1.add a task")
        print("2.delete a task")
        print("3.list tasks")
        print("4.quit")
        choice=input("enter your choice: ")
        if (choice=="1"):
            addTask()
        elif (choice=="2"):
            delTask()
        elif (choice=="3"):
            listTasks()
        elif (choice=="4"):
            break
        else:
            print("enter a valid input")
    print("good bye ")
