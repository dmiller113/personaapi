from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
    import glob

    db = session()

    # Put our elements into the db
    for element in element_list:
        db.add(models.Element_Type(name=element))

    # Put our arcana's into the db
    for arcana in arcana_list:
        db.add(models.Entity_Type(name=arcana))

    db.commit()

    # Entities
    for glub in sorted(glob.glob('personaapi/info/*.yml'),
                       key=lambda x: arcana_list.index(
                       x[x.rfind('/')+1:x.rfind('.')].replace('_', ' '))):
        with open(glub, 'rt') as file:
            fools = yaml.load(file)
            for fool in fools:
                model = models.Entity(
                    name=fool['name'],
                    level=fool['level'],
                    strength=fool['strength'],
                    magic=fool['magic'],
                    endurance=fool['endurance'],
                    agility=fool['agility'],
                    luck=fool['luck'],
                    arcana_id=db.query(
                        models.Entity_Type).filter_by(
                        name=fool['entity_type']).one().id
                )
                db.add(model)
                # Save the changes.
                db.flush()

                # Weakness elements
                for element in fool['weaknesses']:
                    el = models.Weakness_Element(
                        entity_id=model.id,
                        element_id=db.query(models.Element_Type).filter_by(
                            name=element.lower()).one().id
                    )
                    model.weaknesses.append(el)
                    db.flush()
                # Resist elements
                for element in fool['resists']:
                    el = models.Resist_Element(
                        entity_id=model.id,
                        element_id=db.query(models.Element_Type).filter_by(
                            name=element.lower()).one().id
                    )
                    model.resists.append(el)
                    db.flush()
                # Void elements
                for element in fool['voids']:
                    el = models.Void_Element(
                        entity_id=model.id,
                        element_id=db.query(models.Element_Type).filter_by(
                            name=element.lower()).one().id
                    )
                    model.voids.append(el)
                    db.flush()
                # Absorb elements
                for element in fool['absorbs']:
                    el = models.Absorb_Element(
                        entity_id=model.id,
                        element_id=db.query(models.Element_Type).filter_by(
                            name=element.lower()).one().id
                    )
                    model.absorbs.append(el)
                    db.flush()
                # Reflect elements
                for element in fool['repels']:
                    el = models.Repel_Element(
                        entity_id=model.id,
                        element_id=db.query(models.Element_Type).filter_by(
                            name=element.lower()).one().id
                    )
                    model.repels.append(el)
                    db.flush()

    db.commit()
