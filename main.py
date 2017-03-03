from flask import Flask, render_template, request, redirect, url_for
from models.todo import Todo
import os


app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='sosecret',
    DATABASE=os.path.join(app.root_path, 'db.sqlite'),
    SITE_NAME='TO-DO App'
))


@app.route("/")
def list():
    """ Shows list of todo items stored in the database.
    """
    all_tasks = Todo.get_all()
    return render_template('index.html', all_tasks=all_tasks)


@app.route('/new', methods=['GET', 'POST'])
def add():
    """ Creates new todo item
    If the method was GET it should show new item form.
    If the method was POST it should create and save new todo item.
    """
    if request.method == 'POST':
        name = request.form['task']
        task = Todo(0, name)
        task.save()
        return list()
    return render_template('new.html')


@app.route("/remove/<todo_id>")
def remove(todo_id):
    """ Removes todo item with selected id from the database """

    task = Todo.get_by_id(todo_id)
    task.delete()
    return list()


@app.route("/edit/<todo_id>", methods=['GET', 'POST'])
def edit(todo_id):
    """ Edits todo item with selected id in the database
    If the method was GET it should show todo item form.
    If the method was POST it should update todo item in database.
    """
    return "Edit " + todo_id


@app.route("/toggle/<todo_id>")
def toggle(todo_id):
    """ Toggles the state of todo item """
    return "Toggle " + todo_id

if __name__ == "__main__":
    app.run()
