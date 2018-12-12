from flask import Flask, request, render_template, flash, redirect, url_for, session, logging
from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, validators, PasswordField
from passlib.hash import sha256_crypt

app = Flask(__name__)
Articles = Articles()

#Homepage
@app.route('/')
def index():
    return render_template('index.html')

#About Page
@app.route('/about')
def about():
    return render_template('/about.html')

#Articles Page
@app.route('/articles')
def article():
    return render_template('/articles.html', articles=Articles)

@app.route('/article/<string:id>/')
def articles(id):
    return render_template('/article.html', id=id)

#Form
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=30)])
    email = StringField('E-mail', [validators.Length(min=6, max=50)])
    username = StringField('Username', [validators.Length(min=3, max=10)])
    password = PasswordField('PassWord', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='The two passwords should match')
    ])
    confirm = PasswordField('Connfirm Password')

#Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('register.html')
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
