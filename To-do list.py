todo=[]
while True:
    cmd = input("> ")
    if cmd=="help":
        print("Commands:\n-add (adds a task to the bottom of the list)\n-insert (inserts a task above another task)\n-complete (removes a task)\n-view (allows you to see the list)")
    elif cmd=="add":
        theAdd=input("Input task!\n> ")
        todo.append(theAdd)
    elif cmd=="insert":
        theAdd=input("Input task!\n> ")
        theNum=int(input("Where would you like to insert the task?\n> "))
        todo.insert(theNum-1,theAdd)    
    elif cmd=="view":
        for i in range(0,len(todo)):
            print(f"{i+1}. {todo[i]}")
    elif cmd=="complete":
        theDel=int(input("Which task to do you want to delete?\n> "))
        del todo[theDel-1]
