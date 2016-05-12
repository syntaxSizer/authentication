

app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name
