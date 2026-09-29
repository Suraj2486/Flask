from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html") 

@app.route("/submit", methods = ["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")
    # if username == "Naina" and password == "Siya":
    #     return render_template("welcome.html", name = username)
    
    valid_credentials = {
        "Naina" : "naina",
        "Siya" : "siya",
        "Suraj" : "suraj"
    }
    if username in valid_credentials and valid_credentials[username] == password:
        return render_template("welcome.html", name = username)
    else:
        return "Invalid credentials"