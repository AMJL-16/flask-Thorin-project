import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env
# 1st we imported our flask class, last flask with a capital F
# we are importing render_template function from Flask to render html


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
# we are creating an instance of this and storing it in a variable
# called 'app' the 1st argument of the Flask class is the name
# of our module . our package


@app.route("/")
def index():
    return render_template("index.html")
    # return "<h1>Hello,</h1> <h2>World<>"


@app.route("/about")
def about():
    data = []   # initialisation of an empty array called data[]
    with open("data/company.json", "r") as json_data:
        # here we are using a with block with the open function
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
