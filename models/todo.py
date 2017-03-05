import sqlite3


class Todo:
    """ Class representing todo item."""

    def __init__(self, id, name, done):
        self.id = id
        self.name = name
        self.done = done

    def toggle(self, database_path):
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        if self.done == 0:
            self.done = 1
            c.execute("UPDATE tasks SET finished='{}' WHERE id = '{}'".format(self.done, self.id))
        else:
            self.done = 0
            c.execute("UPDATE tasks SET finished='{}' WHERE id = '{}'".format(self.done, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def create_database(database_path):
        """Creates database, drops one if exists."""
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        c.execute('''DROP TABLE IF EXISTS tasks;''')
        c.execute('''CREATE TABLE tasks
                     (id integer primary key autoincrement,
                     task text not null,
                     finished integer);''')
        c.execute('''INSERT INTO tasks(id, task, finished) VALUES (null, "read", 0);''')
        conn.commit()
        conn.close()

    def save(self, database_path):
        """ Saves todo item in database """
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        c.execute('''INSERT INTO tasks(task, finished) VALUES ("{}", "{}");'''.format(self.name, self.done))
        conn.commit()
        conn.close()

    def update(self, database_path):
        """ Updates todo item in database """
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        c.execute("UPDATE  tasks SET task = '{}'  WHERE id = '{}'".format(self.name, self.id))
        conn.commit()
        conn.close()

    def delete(self, database_path):
        """ Removes todo item from the database """
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        c.execute('''DELETE FROM tasks WHERE id = {};'''.format(self.id))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls, database_path):
        """ Retrieves all Todos form database and returns them as list.
        Returns:
            list(Todo): list of all todos
        """
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        all_tasks = c.execute('''SELECT * FROM tasks ORDER BY id;''')
        list_tasks = []
        for row in all_tasks:
            task = Todo(row[0], row[1], row[2])
            list_tasks.append(task)
        conn.close()
        return list_tasks

    @classmethod
    def get_by_id(cls, id, database_path):
        """ Retrieves todo item with given id from database.
        Args:
            id(int): item id
            database_path: os.path.join(app.root_path, 'hello.db')
        Returns:
            Todo: Todo object with a given id
        """
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        cursor_object = c.execute('''SELECT * FROM tasks WHERE id = {};'''.format(id))
        tuple_in_list = cursor_object.fetchall()
        task_by_id = Todo(tuple_in_list[0][0], tuple_in_list[0][1], tuple_in_list[0][2])
        conn.close()
        return task_by_id


