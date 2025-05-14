def get_todos(filepath="todos.txt"):
    """Read a text file and return a list of todo items"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local
def add_todos(filepath, todo):
    with open(filepath, 'a') as file_local:
        file_local.writelines(todo + "\n")
def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

print(__name__)
if __name__ == "__main__":
    print("Hello")
