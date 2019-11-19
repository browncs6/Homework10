#!/usr/bin/python3

from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
# TODO: add imports for database stuff


app = Flask(__name__)
Bootstrap(app)

# TODO: connect to your database and create necessary tables/documents

app.config['SECRET_KEY'] = 'Blah blah blah'

todo_list = []

class AddForm(FlaskForm):
    name = StringField('Task Name', validators=[DataRequired()])
    notes = StringField('Task Notes')
    submit = SubmitField('Submit')


#============================#
# Database Helper Functions! #
#============================#
def get_todo_list_items():
    """Returns a list of all the todo list items from the database"""
    pass

## TODO: insert a todo list item into your daba
def create_item(name, notes):
    """Inserts a todo list item with `name` and `notes` into the database.
    Returns nothing.
    
    Arguments:
        name {string} -- name of todo list item
        notes {string} -- notes of todo list item
    """
    pass

def remove_item(id):
    """Removes a todo list item that has the given `id` from the database.
    Returns nothing.
    
    Arguments:
        id {¯\_(ツ)_/¯} -- the id of the item to be removed; type depends on db
    """
    pass


# TODO: Edit this function so that it inserts the new todo item into the database
#       and pulls most up to date todolist data from the database
@app.route('/', methods=['GET', 'POST'])
def main_page():
    form = AddForm(method="POST")
    if form.validate_on_submit():
        name = form.name.data
        notes = form.notes.data
        form.name.data = ''
        form.notes.data = ''
        todo_list.append({'name': name, 'notes': notes})
    print("LOADING MAIN PAGE")
    print(todo_list)
    return render_template('todo.html', todo_list=todo_list, form=form)

# TODO: Edit this function so that it removes the todo item(s) from the database
#       and pulls most up to date todolist data from the database
@app.route('/remove', methods=['POST'])
def remove_todo():
    print(request.form)
    print(request.form.getlist("boxes"))
    boxes = request.form.getlist("boxes")
    if len(boxes) > 0:
        indices_to_remove = []
        for index in boxes:
            indices_to_remove.append(int(index))
        indices_to_remove.sort()
        indices_to_remove.reverse()
        for i in indices_to_remove:
            del todo_list[i]
    return redirect("/", code=302)


app.run()
