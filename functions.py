FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a todos.txt file and return todo list """
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write list of todos items to a text file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Main function")
