#!/usr/bin/python3
""" Module that starts a Flask App"""
from models import storage
from flask import Flask, render_template


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays the main Hbnb HTML page"""
    states = storage.all("State")
    amenities = storage.all("Amenitity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontent
def teardown(exc):
    """removes all storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
