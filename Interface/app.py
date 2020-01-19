'''
    This is an attempt at an interface for our project using javascript, bootstrap
    and flask.
    All files in interface are for the interface.


'''

# Continue with part 2 tomorrow.
# Mailgun for emails
# https://www.youtube.com/watch?v=zRwy8gtgJ1A&index=1&list=PLillGF-RfqbbbPz6GSEM9hLQObuQjNoj_

from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from functools import wraps
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt


# To read from file
from data import Articles

app = Flask(__name__)

# Config MYSQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rootpass'
app.config['MYSQL_DB'] = 'interface'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#init MySQL
mysql = MySQL(app)

# Don't need to restart server after each change
app.debug = True

# Index
@app.route('/')
def index():
    return render_template('home.html')

# Read from file
Articles = Articles()

# About
@app.route('/about')
def about():
    return render_template('about.html')


# Articles
@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

'''
# Several articles

@app.route('/articles')
def articles():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    result = cur.execute("SELECT * FROM articles")

    articles = cur.fetchall()

    # if we get rows back
    if result > 0:
        return render_template('articles.html', articles=articles)
    else:
        msg = 'No Articles Found'
        return render_template('articles.html', msg=msg)

    # Close connection to db
    cur.close()
'''

'''
# Send the Companies to choose from
@app.route('/companies')
def articles():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    result = cur.execute("SELECT * FROM articles")

    articles = cur.fetchall()

    # if we get rows back
    if result > 0:
        return render_template('articles.html', articles=articles)
    else:
        msg = 'No Articles Found'
        return render_template('articles.html', msg=msg)

    # Close connection to db
    cur.close()
'''

# Single article
@app.route('/article/<string:id>/')
def article(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get article
    result = cur.execute("SELECT * FROM articles WHERE id=%s",[id])

    article = cur.fetchone()


    return render_template('article.html', article=article)




# Register Form class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match.')
    ])
    confirm = PasswordField('Confirm Password')


# User register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.hash(str(form.password.data))

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user and email for checking
        result_username = cur.execute("SELECT * FROM users WHERE username=%s", [username])
        result_email = cur.execute("SELECT * FROM users WHERE email=%s", [email])


        # If we get any data from db
        if not(result_username > 0) and not(result_email > 0):

            # Execute query
            cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name,email,username,password))

            # Commit to # DB
            mysql.connection.commit()

            # Close connection
            cur.close()

            flash('You are now registered and can log in', 'success')

            return redirect(url_for('index'))

            return render_template('register.html', form=form)
        elif (result_username > 0):
            error = 'Username already registered.'
            return render_template('register.html', form=form, error=error)
        else:
            error = 'Email already registered.'
            return render_template('register.html', form=form, error=error)


    return render_template('register.html', form=form)

# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor for database
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username=%s", [username])

        # If we get any data from db
        if result > 0:
            # Get stored hash for password
            data = cur.fetchone()
            password = data["password"]

            # Compare Passwords
            if sha256_crypt.verify(password_candidate,password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection to db
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')

# Check if user is logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out.', 'success')
    return redirect(url_for('login'))

# Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    result = cur.execute("SELECT * FROM articles")

    articles = cur.fetchall()

    # if we get rows back
    if result > 0:
        return render_template('dashboard.html', articles=articles)
    else:
        msg = 'No Articles Found'
        return render_template('dashboard.html', msg=msg)

    # Close connection to db
    cur.close()


# Article Form class
class ArticleForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=200)])
    body = TextAreaField('Body', [validators.Length(min=30)])


# Add Article
@app.route('/add_analysis', methods=['GET', 'POST'])
@is_logged_in
def add_analysis():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data;
        body = form.body.data;

        # Create database cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO articles(title, body, author) VALUES(%s, %s, %s)", (title, body, session['username']))

        # Commit to db
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('Article Created', 'success')

        return redirect(url_for('dashboard'))

    return render_template('add_analysis.html', form=form)


# Edit Article
@app.route('/edit_article/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_article(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get article by id
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])

    article = cur.fetchone()

    # Get form
    form = ArticleForm(request.form)

    # Populate article form fields
    form.title.data = article['title']
    form.body.data = article['body']

    if request.method == 'POST' and form.validate():
        title = request.form['title']
        body = request.form['body']

        # Create database cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("UPDATE articles SET title = %s, body= %s WHERE id = %s", (title, body, id))

        # Commit to db
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('Article Updated', 'success')

        return redirect(url_for('dashboard'))

    return render_template('edit_article.html', form=form)

# Delete Article
@app.route('/delete_article/<string:id>', methods=['POST'])
@is_logged_in
def delete_article(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Execute query
    cur.execute("DELETE FROM articles WHERE id = %s", [id])

    # Commit to db
    mysql.connection.commit()

    # Close connection to db
    cur.close()

    flash('Article Deleted', 'success')

    return redirect(url_for('dashboard'))


if __name__=='__main__':
    app.secret_key='secret123'
    app.run()
