#!web_project/flask/bin/python
from flask import Flask,render_template
#from flask.ext.script import Manager
#from flask.ext.moment import Moment
#from datetime import datetime
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required
#moment = Moment(app)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

#manager = Manager(app)


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    password=PasswordField('PassWord',validators=[Required()])
    submit = SubmitField('Submit')



"""
@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())
"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500



if __name__ == '__main__':
 #  manager.run()
    app.run(debug=True)
