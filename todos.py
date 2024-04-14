
while True:

    user_action = input("\nType add, show, edit, complete or exit. -> ")
    user_action = user_action.strip()

    match user_action:

        case 'add':
            todo = input('\nEnter a todo: ') + "\n"

            with open('todo.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todo.txt', 'w') as file:
                todos = file.writelines(todos)

        case 'show':
            file = open('todo.txt', 'r')
            todos = file.readlines()
            file.close()
            # THIS IS THE LONG METHOD
            # new_todos = []
            # for items in todos:
            #     item = items.strip("\n")
            #     new_todos.append(item)
            # CODE BELOW IS THE LIST COMPREHENSION CODES
            # new_todos = [items.strip('\n') for items in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1} - {item.capitalize()}"
                print(row)

        case 'edit':
            number = int(input("\nNumber of todos to edit. "))
            index = number - 1

            with open('todo.txt', 'r') as file:
                todos = file.readlines()
            new_todo = input("Enter new todo.") + '\n'
            todos[index] = new_todo

            with open('todo.txt', 'w') as file:
                todos = file.writelines(todos)

        case 'complete':

            number = int(input("\nNumber of todos to complete. "))

            with open('todo.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip()
            todos.pop(index)

            with open('todo.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todos {todo_to_remove} was successfully removed."
            print(message)

            # number = number - 1 = this code does not work
            # todos.pop(number) = this code does not work

        case 'exit':

            print("Exiting...goodbye! 👋")
            print("Done")
            break
