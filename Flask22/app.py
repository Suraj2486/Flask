from flask import Flask, render_template, redirect, url_for, flash, request
from forms import RegistrationForm

app = Flask(__name__)
app.secret_key = "Naina"

@app.route("/", methods = ["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f"welcome {name}.. Registration successful")
        return redirect(url_for("success"))
    return render_template("register.html", form = form)

@app.route("/success")
def success():
    return render_template("success.html")