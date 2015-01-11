from personaapi import app, session
from flask import g


@app.before_request
def before_request():
    g.db = session()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route('/')
def hallo():
    return 'hallo sir'
