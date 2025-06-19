todolist= []

def AddTask():
    task = input ('Enter your task: ')
    todolist.append({'task': task, 'status': 'pending'})


def DelTask():
    if len(todolist) == 0:
        print ('The list is empty.')
    else:
        try:
            del_num = int (input('Enter the index of the task you want to delete: '))-1
            if 0<= del_num <= len(todolist):
                del todolist[del_num]
                print (todolist)
            else:
                print ('Out of range.')
        except:
            print ('Invalid output.')


def ShowTask():
    if len(todolist) == 0:
        print ("The list is empty.")
    else:
        for index, task in enumerate(todolist, 1):
            print (f"{index}. {task['task']} - {task['status']}\n")


def CompTask():
    
if __name__ == '__main__':

    print ("This is a ToDoList program.")
    print ("Enter your choice in numbers.") 

    choice = input("""1. Add task \n2. Delete task. \n3. Show Tasks \n4. Mark a task as complete \n5. Quit""")

    if choice == 1:
        AddTask()

    elif choice == 2:
        DelTask()

    elif choice == 3:
        ShowTask()

    #elif choice == 4:
      #  CompTask()

    elif choice == 5:
        exit()

    else:
        print ("Enter a valid response.")
