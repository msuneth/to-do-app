import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

intro_text = """
This is a todo app
Please follow below steps
"""
print(intro_text)
while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        # todo = input(user_prompt) + "\n"
        todos = functions.get_todos()
        todos.append(todo)

        functions.write_todos(todos)
    elif user_action.startswith("show"):
        todos = functions.get_todos()
        # new_todos=[]
        # for todo in todos:
        #     new_todo=todo.strip('\n')
        #     new_todos.append(new_todo)
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            show_string = f'{index + 1}-{item}'
            print(show_string)
    elif user_action.startswith("edit"):
        try:
            # number = int(input("Enter todo number to edit:"))
            number = int(user_action[5:]) - 1
            todos = functions.get_todos()

            new_todo = input("Enter new todo:")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Invalid edit")
            continue
    elif user_action.startswith("complete"):
        try:
            # number = int(input("Enter completed todo number:"))
            number = int(user_action[9:]) - 1  # number - 1
            todos = functions.get_todos("todos.txt")
            todo_tobe_removed = todos[number].strip('\n')
            todos.pop(number)
            print(f"to do '{number + 1}-{todo_tobe_removed}' removed")
            functions.write_todos(todos)

        except IndexError:
            print("You entered non existing todo number")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command not found!")
