import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo'] + '\n'
    print(new_todo)
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter todo item",
              key='new_todo', on_change=add_todo)
