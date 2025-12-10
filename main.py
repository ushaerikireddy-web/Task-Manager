
to_do_list=[]

def add_task():
    print("New task is adding...")
    task=input("Enter a task : ")
    to_do_list.append({"Task":task,"Status":"Pending"})
    print("New task is added.")
    print("\n")


def view_task():
    if len(to_do_list)==0:
        print("No pending tasks . ")
    else:
        print("All tasks are : ")
        for index,task in enumerate(to_do_list,1):
            print(f"{index} : {task['Task']} - {task['Status']}")
    print("\n")



def remove_task():
    if len(to_do_list)==0:
        print("No tasks Found...")
    else:
        try:
            remove_index_val=int(input("Enter index value to remove : "))-1
            if 0<=remove_index_val < len(to_do_list):
             remove_task =to_do_list.pop(remove_index_val)
             print(f"Removed task is{remove_task}")
            else:
                print("Invalid index number. Try again. ")
        except ValueError:
            print("Invalid task number. Please enter a valid task number.")
        print("\n")
def mark_a_task_complete():
    try:
        completig_task_status_index=int(input("Enter  index number : "))-1
        if 0<=completig_task_status_index<len(to_do_list):
            to_do_list[completig_task_status_index]['Status']="Completed"
            print(f"Task {to_do_list[completig_task_status_index]['Task']} has been marked as Completed")
        else:
            print("Invalid index number. Try again...")
    except ValueError:
        print("Please enter a valid task number...")
    print("\n")


        
def exit_task():
    print("Task is Existing...")


def task_manager():
    
    while (True):

        print("1.Add a new task")
        print("2.View the tasks")
        print("3.Remove the task")
        print("4.Mark a task as complete")
        print("5.Exit")

        try:
            choose=int(input("Enter a task num you want : "))


            if choose== 1:
                add_task()
            elif choose==2:
                view_task()
            elif choose==3:
                remove_task()
            elif choose==4:
                mark_a_task_complete()
            elif choose==5:
                exit_task()
                break
        except :
            print("Invalid value , choose any of 1 to 5 number only and try again...")


task_manager()