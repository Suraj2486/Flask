from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)
app.secret_key = "Naina"

# login
@app.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
    
        if username == "Siya" and password == "34568":
            session["user"] =username #stored in session
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials..", mimetype="text/plan") #bydefault html in mimetype

    return '''
        <h2>Login page</h2>
        <form method="POST">
            Username: <input type="text" name = "username"><br>
            Password: <input type="password" name = "password"><br>
            <input type = "submit" value = "login">
        </form>
    '''

@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
            <h2> Welcome, {session["user"]}..</h2>
            <a href={url_for('logout')}>logout</a>
        '''
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
