from flask import Flask, render_template, redirect, url_for, flash, request

app = Flask(__name__)
app.secret_key = "Naina"

@app.route("/", methods = ["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        if not name:
            flash("name can not be empty")
            return redirect(url_for("form"))
        flash(f"thanks, {name} your feedback is saved")
        return redirect(url_for("thankyou"))
    return render_template("form.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")