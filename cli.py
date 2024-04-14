# from functions import get_todo, functions.write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

while True:

    user_action = input("\nType add, show, edit, complete or exit. -> ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        # todos = get_todos()
        todos = functions.get_todo()

        todos.append(todo + "\n")

        functions.write_todos(todos)
        # open_file('tod.txt', 'w')
        # with open('tod.txt', 'w') as file:
        #     todos = file.writelines(todos)

    elif user_action.startswith('show'):

        # todos = get_todos()
        todos = functions.get_todo()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item.capitalize()}"
            print(row)

    elif user_action.startswith('edit'):

        try:
            number = int(f"{user_action[5:]}")
            index = number - 1

            todos = functions.get_todo()
            new_todo = input("Enter new todo -> ") + "\n"

            todos[index] = new_todo

            functions.write_todos(todos)
            # with open('tod.txt', 'w') as file:
            #     todos = file.writelines(todos)
        except ValueError:
            print("Your command is not valid ")
            continue

    elif user_action.startswith('complete'):

        try:
            number = int(f"{user_action[9:]}")

            index = number - 1

            todos = functions.get_todo()

            todo_to_remove = todos[index].strip()
            todos.pop(index)

            functions.write_todos(todos)

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
