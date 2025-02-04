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


while True:
     action = input('Would you like to add, show, complete, edit or exit your todo list? (Type add/new + (todo)/show/edit + (todo number)/complete + (todo number)/exit) ')
     action = action.strip()

     if action.startswith('add'):
          user_input1 = action[4:] + '\n'              # list slicing - user_input1 = action[4:]
          todo_list = get_todos()
          todo_list.append(user_input1.capitalize())
          write_todos(todo_list)

     elif action.startswith('show'):
          todo_list = get_todos()
          for index, i in enumerate(todo_list):
               i = i.strip()
               print(f'{index + 1}. {i}')
          action1 = input('Would you like to exit? (y/n) ')                     #.read() for strings, .readlines() for lists
          action1 = action1.strip()  
          if action1 == 'y':
               print('Bye!')
               break
     
     elif action.startswith('edit'):
          try:
               todo_list = get_todos()
               action2 = action.strip('edit ')
               for i in todo_list:
                    number = int(action2) 
                    number = number - 1                                       # str.repalce(a,b,1) to change words in a string
                    print(f'{action2}. {todo_list[number]}')
                    todo_to_change = todo_list[number]
                    action3 = input('What would you like to change it to? ')
                    action3 = action3.strip()     #fstrings f'{variable}string {variable}}' space depending on your needs
                    todo_list[number] = f'{action3.capitalize() + '\n'}' 
                    changed_todo = todo_list[number]
                    print(f'{todo_to_change.strip('\n')} has been changed to {changed_todo}')
                    write_todos(todo_list)
                    break
          except ValueError:
               print('Your command is invalid!')
               continue
          except IndexError:
                print('You can only edit avaliable todos!')

     elif action.startswith('complete'):
          try:
               todo_list = get_todos()
               action4 = action.strip('complete ')
               action4 = action4.strip()
               action4 = int(action4) - 1
               completed_todo = todo_list[action4].strip('\n')
               todo_list.pop(action4)
               write_todos(todo_list)
               print(f'{completed_todo} marked as completed')
          except IndexError:
               print('You can only complete available todos!')
               continue
          except ValueError:
                print("You must enter a number after 'complete' command!")

     elif action.startswith('exit'):
          print('Bye!')
          break

     else:
          print('Unknown Command!')