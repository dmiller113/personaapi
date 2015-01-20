from personaapi import app, session
from flask import g, jsonify
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.inspection import inspect
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


@app.route(rule=app.config['API_ENDPOINT'] + '<model_type>/<int:id>')
def return_entity(model_type, id):
    try:
        model = g.db.query(getattr(models, model_type)).filter_by(id=id).one()
    except AttributeError:
        return ("Incorrect Route", 404,)
    except NoResultFound:
        return ("ID: %s not found for %s" % (id, model_type), 404,)
    return_type = model.get_return_response()
    return jsonify(return_type)
