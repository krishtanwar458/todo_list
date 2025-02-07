def get_todos(filepath = 'todos.txt'):
     """ Read a text file and return the list of
     to-do items. """
     with open(filepath, 'r') as file_local:
               todo_list_local = file_local.readlines()
     return todo_list_local

def write_todos(todo_list_local, filepath = 'todos.txt'):
     """ Write the to-do items list in a text file. """
     with open(filepath, 'w') as file:
               file.writelines(todo_list_local)