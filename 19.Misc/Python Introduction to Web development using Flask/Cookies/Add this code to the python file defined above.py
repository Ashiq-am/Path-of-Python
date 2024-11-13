from urllib import request

from flask import make_response, render_template, app


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('cookie.html'))
        resp.set_cookie('userID', user)
        return resp


@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome ' + name + '</h1>'
