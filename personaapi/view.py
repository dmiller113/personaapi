from personaapi import app, session
from flask import g, render_template


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


@app.route(rule='/entity/<int:id>')
def return_entity(id):
    from personaapi.models import Entity
    entity = g.db.query(Entity).filter_by(id=id).one()
    col_names = [
        'Arcana', 'Level', 'Strength', 'Magic', 'Endurance',
        'Agility', 'Luck',
    ]
    return render_template('listview.html',
                           entity=entity,
                           list_name="Entity",
                           columns=col_names,
                           getattr=getattr)
