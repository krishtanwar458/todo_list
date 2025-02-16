import streamlit as st  #/Library/Frameworks/Python.framework/Versions/3.13/bin/streamlit run /Users/krishtanwar/Desktop/Python/app/web.py 
import functions

todos = functions.get_todos()

st.title('Todo App')

for index, todo in enumerate(todos):
    st.checkbox(todo, key=f'todo_{index}')

st.text_input(label='Enter a todo:', placeholder='Add a new todo')

