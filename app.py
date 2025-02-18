from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "your_secret_key"


#Configure SQL Alchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Database Model
class User(db.Model):
    # Class variables
    __tablename__="user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

#create data class ~ one unit/row of data
class MyTask(db.Model):
    __tablename__="my_task"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    # we need to give data back to visually see on the screen - using Dunder method
    def __repr__(self) -> str:
        return f"Task{self.id}"


#Routes
@app.route("/")
def home():
    # if user is logged in = in session, redirect to different page -> dashboard.html, otherwise go to index.html
    if "username" in session:
        return redirect(url_for('task'))
    return render_template("index.html")


#Login
@app.route("/login", methods=["POST"])
def login():
    #Collect info from form
    username = request.form['username']
    password = request.form['password']
    #Check if it's in the db
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['username'] = username
        return redirect(url_for('task'))
    else:
        #otherwise show home page
        return render_template("index.html")


#Register
@app.route("/register", methods=["POST"])
def register():
    #Collect info from form
    username = request.form['username']
    password = request.form['password']
    #Query if user is in the db
    user = User.query.filter_by(username=username).first()
    #if user is True = if they're already in the db
    if user:
        return render_template("index.html", error="User already registered.")
    # else create new user
    else:
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        session['username'] = username
        return redirect(url_for('task'))


#Dashboard
@app.route("/dashboard")
def dashboard():
    if "username" in session:
        return render_template("tasks.html", username=session['username'])
    return redirect(url_for('home'))

#tasks - taskmanager
@app.route("/tasks",methods=["GET","POST"])
def task():
    if "username" not in session:
        # Redirect to login page if not logged in
        return redirect(url_for('home'))

    # Get the logged-in username
    username = session["username"]

    # Add a task
    if request.method =="POST":
        current_task = request.form["content"]
        if not current_task.strip():
            return redirect(url_for('task'))
        new_task = MyTask(content=current_task)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('task'))


    tasks = MyTask.query.order_by(MyTask.created).all()
    return render_template("tasks.html", tasks=tasks, username=username)


# Deleting a task
@app.route("/delete/<int:id>")
def delete(id:int):
    if "username" not in session:
        return redirect(url_for('home'))

    task_to_delete = MyTask.query.get_or_404(id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('task'))


# Edit a task
@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id:int):
    if "username" not in session:
        return redirect(url_for('home'))

    task = MyTask.query.get_or_404(id)
    if request.method =="POST":
        task.content = request.form["content"]
        db.session.commit()
        return redirect(url_for('task'))
    return render_template('edit.html',task=task)



#Logout
@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))




if __name__ == "__main__":
    app.run(debug=True)
