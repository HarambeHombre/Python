# Flask To-Do List App - ![Python](https://img.shields.io/badge/Python-3.9-green) ![HTML](https://img.shields.io/badge/HTML-5-orange)

**Flask To-Do List App** is a simple web application that allows users to create and manage a to-do list. The app provides functionality to add tasks and delete tasks, utilizing Python's Flask web framework.

---

## Features

- Add tasks to the to-do list.
- Display all tasks in a list format.
- Delete tasks individually by clicking a delete link.
- Lightweight and easy-to-extend Flask application.

---

## Prerequisites

Before running this application, ensure the following are installed:

1. **Python 3.8 or higher** - Download Python [here](https://www.python.org/downloads/).
2. **Flask Framework** - Install Flask via pip:
   ```bash
   pip install flask
   ```
   
---

## Installation and Setup
1. Clone or download this repository to your local machine.
2. Install the required library:
 ```bash
pip install flask
```
3. Create a new HTML template file named index.html in a folder named templates located in the same directory as the script. Use the following structure for the file:
```Html
<!DOCTYPE html>
<html>
<head>
    <title>To-Do List</title>
</head>
<body>
    <h1>To-Do List</h1>
    <form method="POST">
        <input type="text" name="todo" placeholder="Enter a to-do item" required>
        <button type="submit">Add</button>
    </form>
    <ul>
        {% for key, value in todo_list.items() %}
        <li>{{ value }} <a href="/delete/{{ key }}">Delete</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```
4. Run the script:
   ```bash
   python main.py
   ```

---

## Usage
1. **Add To-Do Items**:
   - Open the app in your browser (default URL: `http://127.0.0.1:5000`).
   - Enter a to-do item in the input field and click "Add."

3. **View To-Do List**:- Newly added items will appear in the list.

4. **Delete To-Do Items**:- Click the "Delete" link next to any item to remove it from the list.

---

## Code Breakdown
### Import Libraries
The script starts by importing Flask and necessary components:
```Python
from flask import Flask, render_template, request, url_for, redirect
```

### Routes
The application defines two routes:
1. Home Route (`/`):
   - Handles GET and POST requests.
   - Displays the current to-do list.
   - Adds new to-do items when the form is submitted.
  ```Python
@app.route('/', methods=["GET", "POST"])
```
2. Delete Route (`/delete/<int:item>`):
   - Deletes the specified to-do item using its key.
   - Redirects back to the home page.
  ```Python
@app.route('/delete/<int:item>', methods=["GET"])
```

### Global Variables
The script uses a global dictionary (`todo_list`) to store to-do items and a counter (`i`) as unique keys:
```Python
todo_list = {}
i = 0
```

### Running the Application
Runs the Flask app locally with debug mode enabled:
```Python
if __name__ == '__main__':
    app.run(debug=True)
```

---

## Example Output
The application provides an intuitive interface:
1. Initial View:
```
To-Do List
[Input Field for To-Do Items]
```
2. To-Do Items:
```
- Item 1 [Delete]
- Item 2 [Delete]
```

---

## Notes
- **Data Persistence**: Currently, the application uses an in-memory dictionary. Data will be lost upon restarting the app.
- **Custom Styling**: You can improve the appearance by adding CSS to the `index.html` file.
- **Scalability**: To make the app scalable, integrate a database for data storage.



   
