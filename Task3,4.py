# Задание 3

class TodoList:
    tasks = []

    def add_task(self, act):
        tasks.append(act)

todo_list = TodoList()
todo_list.tasks = ['Купить лампочку', 'Поменять лампочку', 'Выкинуть лампочку']

print("\n".join(todo_list.tasks))

# Задание 4

class DataBase:
    def __new__(cls, *args, **kwargs):
        return

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")

db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)
print(db is db2)