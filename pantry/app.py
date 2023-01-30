"""
Code to handle user authentication via AWS Cognito
"""

from flask import (Flask, redirect, render_template, request, session,
                   url_for)
from flask_cognito_auth import (CognitoAuthManager, callback_handler,
                                login_handler, logout_handler)
from pantry.groceries import GroceryListHandler

app = Flask(__name__)
app.secret_key = "secret_key"

app.config.from_pyfile("config/cognito_config.py")

cognito = CognitoAuthManager(app)

grocery_list_handler = GroceryListHandler()


@app.route('/')
def home():
    try:
        _ = session["username"]
        return render_template("index.html")
    except KeyError:
        return redirect(url_for("cognitologin"))


@app.route("/grocery-list/update", methods=["POST"])
def update_list():
    current_user = session["username"]
    item = request.get_json()
    grocery_list_handler.update_item(current_user, item)
    return item, 200


@app.route("/grocery-list/get", methods=["GET"])
def get_list():
    current_user = session["username"]
    grocery_list = grocery_list_handler.get_list(current_user)
    return grocery_list, 200


@app.route("/grocery-list/remove", methods=["POST"])
def remove_item():
    current_user = session["username"]
    item = request.get_json()['item']
    grocery_list_handler.remove_item(current_user, item)
    return item, 200


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
    app.run(host="0.0.0.0")
