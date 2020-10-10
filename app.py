from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
# from flask.ext.mysql import MySQL

# mysql = MySQL()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:1234@localhost/flaskapp"
db = SQLAlchemy(app)


# app.config["MYSQL_HOST"] = "127.0.0.1"
# app.config["MYSQL_PORT"] = "3306"
# app.config["MYSQL_USER"] = "root"
# app.config["MYSQL_PASSWORD"] = "1234"
# app.config["MYSQL_DB"] = "flaskapp"
# mysql.init_app(app)

# conn = mysql.connect()

# cursor = conn.cursor()

# db = MySQL(app)
# db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.String(500))

@app.route("/")
def index():
    post = Post.query.all()
    
    return render_template("index.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)