from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def student():
    return render_template("student.html",
                           name = "Naina",
                           is_topper = True,
                           subjects = ["Maths", "Science", "Physics"])