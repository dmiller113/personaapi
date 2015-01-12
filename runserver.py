from personaapi import app, engine, setup
from personaapi.models import Base

import sys


if __name__ == '__main__':
    argument_list = sys.argv[1:] if len(sys.argv) > 1 else [None]

    if argument_list[0] == 'init':
        print("foo")
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        setup()

    app.run(port=7070)
