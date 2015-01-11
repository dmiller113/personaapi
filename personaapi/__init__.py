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
