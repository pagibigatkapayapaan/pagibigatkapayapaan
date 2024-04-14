while True:

    user_action = input("\nType add, show, edit, complete or exit. -> ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]

        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todo.txt', 'w') as file:
            todos = file.writelines(todos)

    if 'show' in user_action:

        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item.capitalize()}"
            print(row)

    if 'edit' in user_action:

        number = int(f"{user_action[4:]}")
        index = number - 1

        with open('todo.txt', 'r') as file:
            todos = file.readlines()
        new_todo = input("Enter new todo -> ") + "\n"

        todos[index] = new_todo

        with open('todo.txt', 'w') as file:
            todos = file.writelines(todos)

    if 'complete' in user_action:
        number = int(input("\nNumber of todos to complete. "))
        index = number - 1

        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        todo_to_remove = todos[index].strip()
        todos.pop(index)

        with open('todo.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todos {todo_to_remove} was successfully removed."
        print(message)

        # number = number - 1 = this code does not work
        # todos.pop(number) = this code does not work

    if 'exit' in user_action:
        print("Exiting...goodbye! 👋")
        print("Done")
        break
