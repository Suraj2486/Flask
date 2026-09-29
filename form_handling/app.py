from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/feedback", methods = ["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("username")
        msg = request.form.get("msg")

        return render_template("thankyou.html", user = name, msg = msg)
    return render_template("feedback.html")