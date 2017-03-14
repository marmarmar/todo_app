from flask import Flask, render_template, request, redirect
from models.todo import Todo
import os


app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='sosecret',
    DATABASE=os.path.join(app.root_path, 'hello.db'),
    SITE_NAME='TO-DO App'
))

DATABASE_PATH = os.path.join(app.root_path, 'hello.db')


def create_database():
    Todo.create_database(DATABASE_PATH)


@app.route("/")
def list():
    """ Shows list of todo items stored in the database.
    """
    all_tasks = Todo.get_all(DATABASE_PATH)
    return render_template('index.html', all_tasks=all_tasks)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """ Creates new todo item
    If the method was GET it should show new item form.
    If the method was POST it should create and save new todo item.
    """
    if request.method == 'POST':
        name = request.form['task']
        task = Todo(None, name, 0)
        task.save(DATABASE_PATH)
        return redirect("/")
    return render_template("add.html")


@app.route("/remove/<todo_id>")
def remove(todo_id):
    """ Removes todo item with selected id from the database """
    task = Todo.get_by_id(todo_id, DATABASE_PATH)
    task.delete(os.path.join(app.root_path, 'hello.db'))
    return redirect("/")


@app.route("/edit/<todo_id>", methods=['GET', 'POST'])
def edit(todo_id):
    """ Edits todo item with selected id in the database
    If the method was GET it should show todo item form.
    If the method was POST it should update todo item in database.
    """
    if request.method == 'POST':
        old_task = Todo.get_by_id(todo_id, DATABASE_PATH)
        name = request.form['name']
        task = Todo(old_task.id, name, old_task.done)
        task.update(os.path.join(app.root_path, 'hello.db'))
        return redirect("/")
    elif request.method == 'GET':
        obj = Todo.get_by_id(todo_id, DATABASE_PATH)
        old_name = obj.name
        return render_template('update.html', old_name=old_name)


@app.route("/toggle/<todo_id>")
def toggle(todo_id):
    """ Toggles the state of todo item """
    task = Todo.get_by_id(todo_id, DATABASE_PATH)
    task.toggle(os.path.join(app.root_path, 'hello.db'))
    return redirect("/")


if __name__ == "__main__":
    create_database()
    app.run()

