# Задание 3

class TodoList:
    tasks = []

    def add_task(self, act):
        tasks.append(act)

todo_list = TodoList()
todo_list.tasks = ['Купить лампочку', 'Поменять лампочку', 'Выкинуть лампочку']

print("\n".join(todo_list.tasks))