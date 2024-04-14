import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do ")
input_box = sg.InputText(tooltip="Enter a to-do item", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todo(),
                      key="todos",
                      enable_events=True, size=[45, 6])
edit_button = sg.Button("Edit")


window = sg.Window('My To-do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("Helvetica", 17))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todo()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        case sg.WIN_CLOSED:
            break

window.close()

