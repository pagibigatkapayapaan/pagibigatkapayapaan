def get_todo(filepath='todo.txt'):
    """Read the text file and return the list of todos items."""
    with open(filepath, 'r') as f:
        todos_local = f.readlines()

    return todos_local


def write_todos(todos_arg, filepath='todo.txt'):
    """Write the to-dos items list into the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
