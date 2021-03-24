#Making a to-do management file

#Ask to operator
print("Welcome to todo-management!")
def print_name(name):
    print("Hello"+" "+name.capitalize())
print_name(input("Enter your name : "))

#Asking the operator
text = "There is already a todo file.\nType 'yes' to open it.\nType 'no' to create a new file."
print(text)

answer = input("Do you want to open the todo file? ")
 
if answer.capitalize()  == "Yes":
    file = open("todo.txt","r")
    file.close()

    #asking to operate
    help_text = "Press 1 to see all the todos\nPress 2 to add a todo\nPress 3 to remove a todo"
    choice = input(help_text + "\n>")
    if choice == "1":
        file = open("todo.txt","r+")
        #get the todos as an array
        todos = file.read().split("\n")
        #remove empty strings from the array
        todos.remove('')
        #if there are no todos
        if len(todos) == 0:
            print("Sorry! there is no todos exists at the moment.")
            exit()
        #print the todos
        for i in range(0,len(todos)):
            print(f"[{i+1}] {todos[i]}")
        #close the file
        file.close()

    elif choice == "2":
       file = open("todo.txt","r")
       todos = file.read().split("\n")
       todos.remove('')
       if len(todos) == 0:
           print("No todos")
       for i in range(0,len(todos)):
           print(f"[{i+1}] {todos[i]}")
       file.close()
       #get the todo to add
       number1 = int(input("How many todos you want to add? "))
       file = open("todo.txt","a")
       for i in range(0,int(number1)):
           todo = input("Enter the todo to add: ")
           entry = f"{todo}\n"
           file.write(entry)
           if i == int(number1)-1:
               print("Done!")
           else:
               print("Okay, next one!")
       file.close()

       print("Your new todo list is: ")
       file = open("todo.txt","r")
       todos = file.read().split("\n") 
       todos.remove('')
       for i in range(0,len(todos)):
           print(f"[{i+1}] {todos[i]}")
       file.close()
       print("Done! All the best!")

    elif choice == "3":
       file = open("todo.txt","r+")
       todos = file.read().split("\n")
       todos.remove('')
       for i in range(0,len(todos)):
           print(f"[{i+1}] {todos[i]}")
       file.close()

       number2 = int(input("How many todos you want to delete?"))
       file = open("todo.txt","r+")
       for i in range(0,int(number2)):
           remove = int(input("Enter the todo number to be deleted: "))
       lines = file.readlines() 
       if i == int(number2)-1:
            print("Done!")
       else:
            print("Okay, next one: ")
       file.close()
    
       for line in lines:
           line = int(remove-1)
       del lines[int(line)]
       new_file = open("todo.txt","w+")
       for line in lines:
           new_file.write(line)
       new_file.close()

       print("The new todo list is: ")
       file = open("todo.txt","r")
       todos = file.read().split("\n")
       todos.remove('')
       for i in range(0,len(todos)):
           print(f"[{i+1}] {todos[i]}")
       file.close()
       print("Done! All the best!")
    else:
       print("That is not a valid option")
       print(help_text)
  
   #Last time reading the file
       print("Your new todo list: ")
       file = open("todo.txt","r")
       todos = file.read().split("\n")
       todos.remove('')
       for i in range(0,len(todos)):
           print(f"[{i+1}] {todos[i]}")
       file.close()
       print("Done! All the best!")

elif answer.capitalize() == "No":
    fname = input("Enter a file name: ")
    number_of_entries = int(input("How many entries do you want to make? "))
    
    file = open(fname,"w+")
    for i in range(0,int(number_of_entries)):
        todo_list = input("Type your todo: ")
        entry = f"{todo_list}\n"
        file.write(entry)
        if i == int(number_of_entries)-1:
           print("Done!")
        else:
           print("Okay, next one: ")
    file.close()
     
    file = open(fname,"r")
    todos = file.read().split("\n")
    todos.remove('')
    for i in range(0,len(todos)):
         print(f"[{i+1}] {todos[i]}")
    file.close()
    print("Done! All the best!")
else:
    print("This is not a valid option.")
    print(text)
