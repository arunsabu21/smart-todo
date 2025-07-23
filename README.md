# 🧠 Smart ToDo

A minimal and intelligent ToDo app built with **Flask + SQLite**, featuring a stylish UI, dark mode, smart suggestions, and modern mobile-first design.

## Features

- Add, complete, edit, and delete tasks
- Mobile-first responsive design (Assistant font)
- Filter tasks by All, Pending, and Completed
- One-click "Mark All as Complete"
- Smart suggestions for productivity (random helpful tips)
- Flash messages with smooth fade effects
- Auto-saves all tasks using SQLite
- Dark mode toggle

## Tech Stack

- Python (Flask)
- SQLite
- HTML, CSS, JavaScript
- Bootstrap 5

## How to Run

```bash
# Clone the repo
git clone https://github.com/arunsabu21/smart-todo.git

cd smart-todo

# Install dependencies (if any)
pip install flask flask_sqlalchemy

# Run the app
python app.py
```

## Code Structure

```
smart-todo/
├── app.py                     # Main Flask app and routes
├── templates/
│   └── index.html             # Main UI template
├── static/
│   └── css/style.css          # Custom styles including dark mode
│   └── images/                # UI images (e.g., no-tasks illustration)
├── todo.db                    # SQLite database (auto-generated)
```

---

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/github/license/arunsabu21/yourrepo)

