import os
from flask import Flask, render_template
# 1st we imported our flask class, last flask with a capital F
# we are importing render_template function from Flask to render html


app = Flask(__name__)
# we are creating an instance of this and storing it in a variable
# called 'app' the 1st argument of the Flask class is the name
# of our module . our package


@app.route("/")
def index():
    return render_template("index.html")
    # return "<h1>Hello,</h1> <h2>World<>"


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
