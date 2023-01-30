"""
Code to handle user authentication via AWS Cognito
"""

from flask import Flask, jsonify, redirect, session, url_for
from flask_cognito_auth import (CognitoAuthManager, callback_handler,
                                login_handler, logout_handler)

app = Flask(__name__)
app.secret_key = "secret_key"

app.config.from_pyfile("config/config.py")

cognito = CognitoAuthManager(app)


@app.route('/home')
def home():
    current_user = session["username"]
    return jsonify(logged_in_as=current_user), 200


@app.route('/callback')
@callback_handler
def aws_cognito_redirect():
    for key in list(session.keys()):
        print(f"Value for {key} is {session[key]}")
    response = redirect(url_for("home"))
    return response


@app.route('/login')
@login_handler
def cognitologin():
    pass


@app.route('/logout')
@logout_handler
def cognitologout():
    pass


if __name__ == '__main__':
    app.run(debug=True)
