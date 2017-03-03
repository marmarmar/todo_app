import sqlite3
import os
import os.path


class Todo:
    """ Class representing todo item."""

    def __init__(self, id, name, done=False):
        self.id = id
        self.name = name
        self.done = done

    def toggle(self):
        """ Toggles item's state """
        self.done = True

    @staticmethod
    def create_database(database_path):
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        c.execute('''DROP TABLE IF EXISTS tasks;''')
        c.execute('''CREATE TABLE tasks
                     (id integer primary key autoincrement,
                     task text not null,
                     finished boolean not null);''')
        c.execute('''INSERT INTO tasks(id, task, finished) VALUES (null, "read", 0);''')
        conn.commit()
        conn.close()

    def save(self):
        """ Saves/updates todo item in database """
        package_dir = os.path.abspath(os.path.dirname("/home/mar/Documents/python-flask-todo-marmarmar/models"))
        database_path = os.path.join(package_dir, 'hello.db')
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        c.execute('''INSERT INTO tasks(task, finished) VALUES ("{}", "{}");'''.format(self.name, self.done))
        conn.commit()
        conn.close()

    def delete(self):
        """ Removes todo item from the database """
        package_dir = os.path.abspath(os.path.dirname("/home/mar/Documents/python-flask-todo-marmarmar/models"))
        database_path = os.path.join(package_dir, 'hello.db')
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        c.execute('''DELETE FROM tasks WHERE id = {};'''.format(self.id))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        """ Retrieves all Todos form database and returns them as list.
        Returns:
            list(Todo): list of all todos
        """
        package_dir = os.path.abspath(os.path.dirname("/home/mar/Documents/python-flask-todo-marmarmar/models"))
        database_path = os.path.join(package_dir, 'hello.db')
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        all_tasks = c.execute('''SELECT * FROM tasks;''')
        list_tasks = []
        for row in all_tasks:
            task = Todo(row[0], row[1], row[2])
            list_tasks.append(task)
        conn.close()
        return list_tasks

    @classmethod
    def get_by_id(cls, id):
        """ Retrieves todo item with given id from database.
        Args:
            id(int): item id
        Returns:
            Todo: Todo object with a given id
        """
        package_dir = os.path.abspath(os.path.dirname("/home/mar/Documents/python-flask-todo-marmarmar/models"))
        database_path = os.path.join(package_dir, 'hello.db')
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        cursor_object = c.execute('''SELECT * FROM tasks WHERE id = {};'''.format(id))
        tuple_in_list = cursor_object.fetchall()
        task_by_id = Todo(tuple_in_list[0][0], tuple_in_list[0][1])
        conn.close()
        return task_by_id


def main():
    # Todo.create_database(os.path.join(app.root_path, 'db.sqlite'))
    print(Todo.get_all())
    # print(Todo.get_by_id(1).name)

main()