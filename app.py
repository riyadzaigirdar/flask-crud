from flask import Flask, render_template, request, redirect, Response, jsonify
from flask_sqlalchemy import SQLAlchemy, BaseQuery
import json

class GetOrQuery(BaseQuery):
    def get_or(self, ident, default=None):
        print(self.get(ident))
        print(ident)
        return self.get(ident) or default

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app, query_class=GetOrQuery)

class Config():
    def __init__(self, **args):
        return super(Post, self).__init__(**args)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return True

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True

    def get(**kwargs):
        print(kwargs)
        return Post.query.filter_by(author="riyadzaigir")  


class Post(db.Model, Config):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(80), nullable=False)
    comment = db.Column(db.String(500), nullable=False)  

    def __repr__(self):
        return "<post: %r>" % self.author

@app.route("/")
def index():
    # get query
    # print(request.args.get('o'))
    # by = request.query_string # give byte string
    # print(json.dumps(by.decode("utf-8")))
    # pagination
    # comments = Post.query.all()[0:1]
    comments = Post.query.all()

    # print(Post.get(id=1))

    return render_template("index.html", comments=comments)

@app.route("/signin")
def sign_page():
    return render_template("sign.html")

@app.route("/process", methods=["POST"])
def process_request():
    name = request.form["name"]
    comment = request.form["comment"]
    new_post = Post(author = name, comment=comment)
    ok = new_post.save()
    
    if ok:
        return redirect("/")

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_item(id):
    obj = Post.query.filter_by(id=int(id))[0]
    obj.delete()
    return jsonify({"message": "Item deleted", "code": 200})

@app.route("/update/<int:id>", methods=["PATCH"])
def update_item(id):
    data = request.data.decode("utf-8")
    data = json.loads(data)
    new_name = data["name"] if data.get("name") else None
    new_comment = data["comment"] if data.get("comment") else None
    obj = Post.query.filter_by(id=int(id))[0]

    obj.author = new_name
    obj.comment = new_comment
    db.session.commit()
    return jsonify({"message": "Item update", "code": 200, "item": { "author": obj.author, "comment": obj.comment }})    

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