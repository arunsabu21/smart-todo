from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'todo124'
# Config SQLite DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# DB Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)


# Create DB
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    filter_type = request.args.get("filter", "all")

    if filter_type == "completed":
        tasks = Task.query.filter_by(completed=True).all()
    elif filter_type == "pending":
        tasks = Task.query.filter_by(completed=False).all()
    else:
        tasks = Task.query.all()
        suggestion = suggest_task()

    return render_template("index.html", tasks=tasks, filter_type=filter_type, suggestion=suggestion)


@app.route('/add', methods=['POST'])
def add():
    content = request.form.get('task')
    if content:
        new_task = Task(content=content)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    flash('Task removed successfully!','success')
    return redirect('/')

@app.route('/complete/<int:id>')
def complete(id):
    task = Task.query.get_or_404(id)
    task.completed = True
    db.session.commit()
    return redirect('/')

@app.route("/edit/<int:task_id>")
def edit_task(task_id):
    new_content = request.args.get("content", "")
    if new_content:
        task = Task.query.get_or_404(task_id)
        task.content = new_content
        db.session.commit()
        flash("Task updated successfully!", "success")
    return redirect("/")

@app.route("/complete_all", methods=["POST"])
def complete_all():
    pending_tasks = Task.query.filter_by(completed=False).all()
    for task in pending_tasks:
        task.completed = True
    db.session.commit()
    return redirect(url_for("index"))

import random

def suggest_task():
    suggestions = [
        "Read a book for 15 minutes",
        "Go for a short walk",
        "Clean your workspace",
        "Call a friend or family member",
        "Plan tomorrow’s goals",
        "Drink a glass of water",
        "Practice deep breathing",
        "Organize your files",
        "Stretch for 5 minutes",
        "Write in a journal"
    ]
    return random.choice(suggestions)




if __name__ == "__main__":
    app.run(debug=True)
