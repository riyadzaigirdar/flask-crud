# CONFIGURE MYSQL in DJANGO AND FLASK

1.Install mysql globally in your computer using your pc's package manager. In my case, using manjaro(for both django and flask)

$ sudo pacman -S mysql

# IMPORTANT: PROCEDURE DETAILS IN THIS LINK -> https://manjaro-tutorial.blogspot.com/2016/11/install-mysql-server-on-manjaro-1610.html?fbclid=IwAR3z8sWjxrtPdyNipu9r7Cy1gpLQYUjFL_JX9vzAv_FP6J46b7WM542rlEk

INCASE YOUR FORGOT YOUR PASSWORD DURING INSTALLATION. YOU JUST NEED TO RESET YOUR PASSWORD NOT YOUR USERNAME BEACAUSE YOU WILL HAVE root USERNAME IN THE MYSQL DATABASE WITH WHICH YOU CAN LOGIN

To reset the password:
Follow these steps (can be helpful if you really forget your password and you can try it anytime, even if you're not in the situation at the moment):

Stop mysql:

$ sudo /etc/init.d/mysql stop

Or for other distribution versions:

$ sudo /etc/init.d/mysqld stop

Start MySQL in safe mode:

$ sudo mysqld_safe --skip-grant-tables &

Log into MySQL using root:

$ mysql -uroot

Select the MySQL database to use:

$ use mysql;

Reset the password:

For MySQL version < 5.7:

$ update user set password=PASSWORD("mynewpassword") where User='root';

For MySQL 5.7:

$ update user set authentication_string=password('mynewpassword') where user='root';

Flush the privileges:

$ flush privileges;

Restart the server:

$ quit

Stop and start the server again:

Ubuntu and Debian:

$ sudo /etc/init.d/mysql stop
$ sudo /etc/init.d/mysql start

On CentOS, Fedora, and RHEL:

$ sudo /etc/init.d/mysqld stop
$ sudo /etc/init.d/mysqld starT

2. Create a database using root login, this database will be used by our framworks flask or django.

Before creating any database link the socket which will be used by MYSQL:

$ ln -s /var/lib/mysql/mysql.sock /tmp/mysql.sock

$ service mysql restart

Login with a new password:

$ mysql -u root -p

Create Database:

-> CREATE DATABASE db <-- db is out database name

Get out of the sql terminal using ctrl+c. Then run the database in localhost using this command:

$ mysql -h 127.0.0.1 -P 3306 -u root -p db

// -h means host which is 127.0.0.1 -P(Capital P) means PORT which is 3306, -u is the user which should always be root unless you create a new user and give all the root privilege to that new user. -p(small p) means the database name we want to run our localhost.

our db named database is running on host localhost, port 3306, user root, database name db and password you know of your root user

now we can use this info to configure our django and flask app

# CONFIGURE YOUR FLASK OR DJANGO APP WITH RUNNING MYSQL DATABASE

# FLASK

3. First Install flask_sqlalchemy: 

(venv)$ pip install flask-sqlalchemy

4. import SQLALCHEMY in your .py file: 

from flask_sqlalchemy import SQLAlchemy

5. set your app configuration with sqlalchemy and mysql: 

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://<username>:<password>@localhost/<db_name>"

6. Initialize db: 

db = SQLAlchemy(app)

7. create a simple model: 

class Post(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(100))
   body = db.Column(db.String(500))

8. open up the python shell:

(venv)$ python

9. import db from your .py file, in mycase app.py: 

> from app.py import db

10. create the database: 

> db.create_all()

# DJANGO

3.Configure settings.py file: 

DATABASES = {  

 'default' : {
 
'ENGINE': 'django.db.backends.mysql',

'NAME': 'db', <--your database name

'USER': 'root',

'PASSWORD': 'your_password',

'HOST': 'localhost',  

 'PORT': '3306',

  }
}

4.Makemigration and Migrate:

(venv)

$ python manage.py makemigrations 


$ python manage.py migrate
