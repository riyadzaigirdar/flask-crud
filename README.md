# connect sqlalchemy with server through pymysql
   [install pymysql](https://stackoverflow.com/questions/22252397/importerror-no-module-named-mysqldb)

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

$ sudo systemctl start mariadb

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

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://username:password@localhost/<db_name>"

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


# Some Common queries in MYSQL

start mysql in system kernel

sudo systemctrl start mariadb

To create the database login as root 

mysql -u root -p

Start server with specific database:

mysql -h 127.0.0.1 -P 3306 -u root -p ecoommerce // Cap P for port and small p for database

To create database use following queries:

CREATE DATABASE db;

To List databases:

SHOW DATABASES;

Delete Database:

DROP DATABASE flaskapp;

# specific database query

login to mysql with only root or running server and tell mysql to use that table

use ecommerce;

show table of that ecommerce database 

show tables;

insert into a category table

INSERT INTO category(id, name) VALUES (1, "jobs"), (2, "rape culture"), (3, "babu tumi khaiso"), (4, "HSC auto pass"), (5, "Chatro doing most rapes");

insert into post table

INSERT INTO post(title, body, categories) VALUES
('TITLE OF POST 1','THIS IS BODY OF POST 1',1),
('TITLE OF POST 2','THIS IS BODY OF POST 2',2),
('TITLE OF POST 3','THIS IS BODY OF POST 3',3),
('TITLE OF POST 4','THIS IS BODY OF POST 4',4),
('TITLE OF POST 5','THIS IS BODY OF POST 5',5),
('TITLE OF POST 6','THIS IS BODY OF POST 6',3),
('TITLE OF POST 7','THIS IS BODY OF POST 7',1);

# important note values should be comma(,) seperated

# you can do additional queries using following queries

1.SELECT name,id FROM category ORDER BY name DESC;

2.SELECT name,id FROM category WHERE id BETWEEN 1 AND 3;

3.SELECT name,id FROM category WHERE name='HSC auto pass' OR name='jobs';

4.SELECT id,name FROM category WHERE name='HSC auto pass';

5.SELECT name FROM employee WHERE employee.dept_code IS NULL;

# DELETE a row from a table

DELETE FROM category WHERE id=7;

6.SELECT emp_id,name,dept_code FROM employee WHERE salary=(SELECT MAX(salary) FROM employee);

# You can query using multiple tables

SELECT id.title, body
FROM post JOIN category
ON category.name = "babu tumi khaiso";

7.SELECT departmet.dept_name, COUNT(employee.emp_id)
FROM departmet JOIN employee
ON employee.dept_code = departmet.dept_code
GROUP BY departmet.dept_name;

8.SELECT AVG(salary) FROM employee;

9.13. SELECT department.dept_code, dept_name FROM employee JOIN department
ON employee.dept_code = department.dept_code GROUP BY( dept_code)
HAVING AVG(salary) > (SELECT AVG(salary) FROM employee);

10.SELECT employee.name FROM employee WHERE LENGTH(employee.name)=4;

11.SELECT name FROM employee WHERE name LIKE 'm%';

12.SELECT name FROM employee WHERE name LIKE 'a%' or name LIKE 'm%';

13.SELECT name,MAX(salary) as salary FROM employee 
WHERE salary < (SELECT MAX(salary) from employee);

14.SELECT salary*2  FROM employee 
WHERE name='aziz';

//third highest

SELECT name,MAX(salary) as salary FROM employee
WHERE salary < (SELECT MAX(salary) FROM employee WHERE salary < (SELECT MAX(salary) FROM employee));








