todo_list = []
completed_list = []

while True:
        action = input('Would you like to add, show, complete, edit or exit your todo list? (Type add/show/edit/complete/exit) ')
        action = action.strip()

        match action:
            case 'add':
                user_input1 = input('Enter a todo: ')
                user_input1 = user_input1.strip()
                todo_list.append(user_input1.capitalize())
                numbered_todo_list = []
                for index, i in enumerate(todo_list):
                     index = index + 1
                     i = i.capitalize()
                     i = f'{index}. {i}'
                     numbered_todo_list.append(i)
            case 'show':
                for index, i in enumerate(todo_list):
                     print(f'{index + 1}. {i}')
                action1 = input('Would you like to exit? (y/n) ')
                action1 = action1.strip()  
                if action1 == 'y':
                     print('Bye!')
                     break
            case 'edit':
                    action2 = input('Which todo number would you like to edit? ')
                    action2 = action2.strip()
                    for i in todo_list:
                          print()
                          number = int(action2)  
                          number = number - 1                                       # str.repalce(a,b,1) to change words in a string
                          print(numbered_todo_list[number])
                          action3 = input('What would you like to change it to? ')
                          action3 = action3.strip()
                          numbered_todo_list[number] = f'{(number + 1)}. {action3.capitalize()}'          #fstrings f'{variable}string {variable}}' space depending on your needs
                          todo_list[number] = f'{action3.capitalize()}' 
                          print('Todo changed')
                          break
            case 'complete':
                  for i in numbered_todo_list:
                       print(i)
                  action4 = input('Which todo number would you like to complete? ')
                  action4 = action4.strip()
                  action4 = int(action4) - 1
                  completed_list.append(todo_list[action4])
                  numbered_todo_list.pop(action4)
                  todo_list.pop(action4)
                  print('todo marked as completed')
                  action5 = input('Would you like to view your list of completed todos? (y/n) ')
                  if action5 == 'y':
                       for index, i in enumerate(completed_list):
                            print(f'{index + 1}. {i}')
            case 'exit':
                  print('Bye!')
                  break
            case _ :
                print('Unknown Command')