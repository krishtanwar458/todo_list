import functions
import FreeSimpleGUI as sg

label = sg.Text('Type in a todo.')
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(values = functions.get_todos(), key='todos', 
                      enable_events=True, size=[45,10])
edit_button = sg.Button('Edit')

window = sg.Window('Todo App', 
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Calibri', 12))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()