from personaapi import app, engine, setup
from personaapi.models import Base

import sys


if __name__ == '__main__':
    argument_list = sys.argv[1:] if len(sys.argv) > 1 else [None]

    if argument_list[0] == 'init':
        print("Initializing the database. Dropping all current tables.")
        Base.metadata.drop_all(engine)
        print("Creating all defined tables.")
        Base.metadata.create_all(engine)
        print("Entering in info from info files.")
        setup()
        print("Setup Done")

    app.run(port=7070)
