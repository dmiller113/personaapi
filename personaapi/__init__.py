from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ipdb

app = Flask(__name__)
app.config.from_object('personaapi.settings')

session = None


engine = create_engine("%s://%s:%s@%s/%s" % (
    app.config["DATABASE_TYPE"],
    app.config["DATABASE_USER"],
    app.config["DATABASE_PASS"],
    app.config["DATABASE_URL"],
    app.config["DATABASE_NAME"]))
session = sessionmaker(bind=engine)
import personaapi.view


def setup():
    global session
    from personaapi import models
    from personaapi.info import element_list, arcana_list
    import yaml
    db = session()

    # Put our elements into the db
    for element in element_list:
        db.add(models.Element_Type(name=element))

    # Put our arcana's into the db
    for arcana in arcana_list:
        db.add(models.Entity_Type(name=arcana))

    # Entities
    with open('personaapi/info/fools.yml', 'rt') as file:
        fools = yaml.load(file)
        for fool in fools:
            db.add(models.Entity(
                name=fool['name'],
                level=fool['level'],
                strength=fool['strength'],
                magic=fool['magic'],
                endurance=fool['endurance'],
                agility=fool['agility'],
                luck=fool['luck'],
                arcana=db.query(
                    models.Entity_Type).filter_by(
                    name=fool['entity_type']).one().id
            ))

    # Save the changes.
    db.commit()
