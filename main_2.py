# from functions import get_todos, add_todos, write_todos
from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"Now it's {now}")

while True:
    user_action = input("Type add, show, edit or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        functions.add_todos("todos.txt", todo)
    elif user_action.startswith("show"):
        todos = functions.get_todos("todos.txt")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todos("todos.txt")
            edited_todos = [f"{index + 1}: {todo.strip('\n')}" for index, todo in enumerate(todos)]
            print(edited_todos)
            number = int(user_action[5:]) - 1
            chosen_todo = todos[number]
            print(f"You chose: {chosen_todo}")
            new_todo = input('Enter a new todo: ') + '\n'
            todos[number] = new_todo
            functions.write_todos("todos.txt", todos)
            print(f"{chosen_todo.strip('\n')} was changed to {new_todo}")
        except ValueError:
            print("You need to enter a NUMBER")
            continue
    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos("todos.txt")
            edited_todos = [f"{index + 1}: {todo.strip('\n')}" for index, todo in enumerate(todos)]
            print(edited_todos)
            number = int(user_action[9:]) - 1
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)
            functions.write_todos("todos.txt", todos)
            print(f"{todo_to_remove} was removed from the list")
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print(f"Hey {user_action} is bad!")


print("Bye")

