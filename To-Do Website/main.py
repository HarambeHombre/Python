from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

todo_list = {}
i = 0
@app.route('/', methods=["GET", "POST"])
def home():
    global i
    if not todo_list:
        i=0
    if request.method == "POST":
        if request.form.get('todo'):
            todo_list[i]= request.form.get('todo')
        else:
            todo_list[i]= "Blank todo"
        i += 1
        return render_template('index.html', todo_list=todo_list)

    return render_template('index.html', todo_list=todo_list)

@app.route('/delete/<int:item>', methods=["GET"])
def delete(item):
    todo_list.pop(item)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)