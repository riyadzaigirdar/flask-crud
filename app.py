from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(80), nullable=False)
    comment = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return "<post: %r>" % self.author

@app.route("/")
def index():
    # get query
    print(request.args.get('o'))
    by = request.query_string # give byte string
    print(json.dumps(by.decode("utf-8")))
    # pagination
    comments = Post.query.all()[0:1]

    return render_template("index.html", comments=comments)

@app.route("/signin")
def sign_page():
    return render_template("sign.html")

@app.route("/process", methods=["POST"])
def process_request():
    name = request.form["name"]
    comment = request.form["comment"]

    new_post = Post(author=name, comment=comment)

    db.session.add(new_post)
    db.session.commit()

    return redirect("/")

@app.route("/home", methods=["GET", "POST"])
def home():
    context = {
        "name": "Riyad",
        "professtion": "Software Developer",
        "Office": "Kalke.co",
        "skills": [
            {
                "name": "marketing"
            },
            {
                "name": "programming"
            },
            {
                "name": "publice relations"
            }
        ]
    }
    return render_template("home.html", context=context)

if __name__ == "__main__":
    app.run(debug=True)