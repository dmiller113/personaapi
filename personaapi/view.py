from personaapi import app, session
from flask import g, jsonify
from sqlalchemy.orm.exc import NoResultFound
from personaapi import models


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


@app.route(rule=app.config['API_ENDPOINT'] + '<type>/<int:id>')
def return_entity(type, id):
    try:
        model = g.db.query(getattr(models, type)).filter_by(id=id).one()
    except AttributeError:
        return ("Incorrect Route", 404,)
    except NoResultFound:
        return ("ID: %s not found for %s" % (id, type), 404,)
    return_type = {}
    for key in model.__table__.columns.keys():
        return_type[key] = getattr(model, key)
    return jsonify(return_type)
