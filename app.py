from flask import Flask, render_template, request

app = Flask(__name__)

comments = []

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/input", methods=["POST"])
def input():
    if request.method == "POST":
        username = request.form.get("username")
        comment = request.form.get("comment")
        comments.append(username + " " + comment)

    return render_template("input.html", comments=comments)

