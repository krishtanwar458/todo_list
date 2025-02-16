import streamlit as st  #/Library/Frameworks/Python.framework/Versions/3.13/bin/streamlit run /Users/krishtanwar/Desktop/Python/app/web.py 
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo.capitalize() + '\n')
    functions.write_todos(todos)

todos = functions.get_todos()

st.title('Todo App')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f'{todo}{index+1}')
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f'{todo}{index+1}']
        st.rerun()

st.text_input(label='Enter a todo:', placeholder='Add a new todo', on_change=add_todo, 
              key='new_todo')
