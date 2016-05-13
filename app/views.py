from flask import Flask, render_template
# ...


@app.route('/index')
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
