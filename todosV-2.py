FILEPATH = 'todo.txt'
while True:

    user_action = input("\nType add, show, edit, complete or exit. -> ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        with open(FILEPATH, 'r') as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open(FILEPATH, 'w') as file:
            todos = file.writelines(todos)

    elif user_action.startswith('show'):

        with open(FILEPATH, 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item.capitalize()}"
            print(row)

    elif user_action.startswith('edit'):

        try:
            number = int(f"{user_action[5:]}")
            index = number - 1

            with open(FILEPATH, 'r') as file:
                todos = file.readlines()
            new_todo = input("Enter new todo -> ") + "\n"

            todos[index] = new_todo

            with open(FILEPATH, 'w') as file:
                todos = file.writelines(todos)
        except ValueError:
            print("Your command is not valid ")
            continue

    elif user_action.startswith('complete'):

        try:
            number = int(f"{user_action[9:]}")

            index = number - 1

            with open(FILEPATH, 'r') as file:
                todos = file.readlines()

            todo_to_remove = todos[index].strip()
            todos.pop(index)

            with open(FILEPATH, 'w') as file:
                file.writelines(todos)

            message = f"Todos {todo_to_remove} was successfully removed."
            print(message)

            # number = number - 1 = this code does not work
            # todos.pop(number) = this code does not work
        except IndexError:
            print("There is no items with that number.")

    elif 'exit' in user_action:
        print("Exiting...goodbye! 👋")

        break

    else:
        print("Invalid input! ❌")

print("Done")
