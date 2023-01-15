"""
This module keeps track of the grocery list.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/add", methods=["POST"])
def add_item():
    # Function to add item to Mongo
    pass


@app.route("/remove", methods=["PUT"])
def remove_item():
    # Function to remove an item
    pass
