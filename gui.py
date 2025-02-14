import functions
import FreeSimpleGUI as sg
import time
import os

if os.path.exists('todos.txt') == False:
    with open('todos.txt', 'w') as file:
        pass

sg.theme('LightBlue7')

Clock = sg.Text('', key='clock')
label = sg.Text('Type in a todo.', key='label')
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add', tooltip='Add a todo') #image instead of ADD label -> sg.Button(image_source=filepath)
list_box = sg.Listbox(values = functions.get_todos(), key='todos', 
                      enable_events=True, size=[35,6])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window('Todo App', 
                   layout=[[Clock], [label], [input_box, add_button], [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Calibri', 12))

while True:
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED:
        break
    window['clock'].update(value=time.strftime('%b %d, %Y | %H:%M:%S'))
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo.capitalize())
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo.capitalize() + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("You must select a todo then make an edit in the input box and then click the 'Edit' button")
                continue
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            try:
                todo_to_compelte = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_compelte)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                window['label'].update("You must select a todo to complete")
        case 'Exit':
            break

window.close()