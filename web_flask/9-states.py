#!/usr/bin/python3
"""This is a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """To print all the cities in the database"""
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def stateId(id):
    """Print states if with id"""
    states = storage.all(State)
    if id:
        st = ""
        for state in states.values():
            if state.id == id:
                st = state
        if st:
            return render_template('9-states.html', state=st)
        return render_template('9-states.html', error='404')
    sort = sorted(states.values(), key=lambda state: state.name)
    return render_template('9-states.html', states=sort)


@app.teardown_appcontext
def close_session(ctx):
    """To remove the current SQL Alchemy"""
    storage.close()


if __name__ == '__main__':
    # app.run(Debug=True)
    app.run(host="0.0.0.0", port=5000)
